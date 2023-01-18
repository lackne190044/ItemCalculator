import sqlalchemy
import sqlalchemy.orm

from model import Base

class DB_Handler:
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
#            session.refresh(item)
        return item

    def bulk_add_to_db(self, items):
        with self.session_factory() as session:
            session.bulk_save_objects(items)
            session.commit()

    def commit_db(self):
        with self.session_factory() as session:
            session.commit()

