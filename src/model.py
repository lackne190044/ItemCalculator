import sqlalchemy
import sqlalchemy.ext.declarative
from sqlalchemy.orm import backref, relationship

Base = sqlalchemy.ext.declarative.declarative_base()


class Item(Base):
    """Item representation."""

    __tablename__ = "item"
    item_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    item_name = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self) -> str:
        return str(self.item_name)


class Recipe(Base):
    """Recipe representation."""

    __tablename__ = "recipe"
    item_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("item.item_id"),
                                nullable=False)
    resource_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("item.item_id"),
                                nullable=False)
    __table_args__ = (sqlalchemy.PrimaryKeyConstraint('item_id', 'resource_id', name='PartofItem'), )

