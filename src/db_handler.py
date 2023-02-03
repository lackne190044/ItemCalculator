import sqlalchemy
import sqlalchemy.orm
from abc import ABC

from src.model import Base, Item

class DB_Handler(ABC):
    def __init__(self, database):
        self.session_factory = self.make_connection(database)

    def make_connection(self, database):
        connection = sqlalchemy.create_engine(database)
        Base.metadata.create_all(connection)
        session_factory = sqlalchemy.orm.sessionmaker()
        session_factory.configure(bind=connection)
        return session_factory

    def add_to_db(self, item):
        """Add Item to database and refresh it."""
        with self.session_factory() as session:
            session.add(item)
            session.commit()
            session.refresh(item)
        return item

    def bulk_add_to_db(self, items):
        with self.session_factory() as session:
            session.bulk_save_objects(items)
            session.commit()

    def search(self):
        raise NotImplemented("search is not implemented")

    def commit_db(self):
        with self.session_factory() as session:
            session.commit()

    def update_item(self, item, new_name):
        with self.session_factory() as session:
            updated = session.query(item).update({item.item_name: new_name})
        return updated

    def remove_item(self, item):
        """Remove Item from database."""
        with self.session_factory() as session:
            session.delete(item)
            session.commit()

