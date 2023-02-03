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
        return f"{self.item_id}: {self.item_name}"


class Recipe(Base):
    """Recipe representation."""

    __tablename__ = "recipe"
    recipe_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    item_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("item.item_id"),
                                nullable=False)
                                # primary_key=True)
    resource_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("item.item_id"),
                                nullable=False)
                                # primary_key=True)
    resource_amount = sqlalchemy.Column(sqlalchemy.Integer)

    def __repr__(self) -> str:
        return f"{self.item_id}: {self.resource_id}|{self.resource_amount}"
    # __table_args__ = (
    #         sqlalchemy.PrimaryKeyConstraint(item_id, resource_id), {},
    #         )

