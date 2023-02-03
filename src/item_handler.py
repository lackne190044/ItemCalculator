from sqlalchemy.sql.operators import is_
from .db_handler import DB_Handler
from .model import Item

class ItemHandler(DB_Handler):
    def search_item(self, item_name: str) -> Item:
        """Search for Item in database."""
        with self.session_factory() as session:
            filtered = (
                session.query(Item)
                .filter(Item.item_name.is_(item_name))
                .all()[0]
                )
        return filtered

    def search_item_by_id(self, item_id: int) -> Item:
        """Search for Item in database."""
        with self.session_factory() as session:
            filtered = (
                session.query(Item)
                .filter(Item.item_id.is_(item_id))
                .all()[0]
                )
        return filtered

