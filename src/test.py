from src.recipe_handler import RecipeHandler


handler = RecipeHandler("sqlite:///items.db")


print(handler.search_item(8))

