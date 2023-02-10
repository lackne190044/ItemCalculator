from .db_handler import DB_Handler
from .model import Recipe

class RecipeHandler(DB_Handler):
    def search_item(self, item_id: int) -> list[Recipe]|None:
        """Search for Item in database."""
        with self.session_factory() as session:
            filtered = (
                session.query(Recipe)
                .filter(Recipe.item_id.is_(item_id))
                .all()
                )
        if len(filtered) < 1:
            return None
        return filtered
