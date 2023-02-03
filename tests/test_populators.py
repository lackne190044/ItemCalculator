from src.populate_items import populate_items
from src.populate_recipes import populate_recipes
from src.item_handler import ItemHandler
from src.recipe_handler import RecipeHandler
from test_handler import TestHandler

import os

def test_populate_items():
    test_handler = TestHandler()

    test_handler.remove_files(["tmp/items.db"])
    test_handler.remove_folders(["tmp"])

    os.mkdir("tmp")
    handler = ItemHandler("sqlite:///tmp/items.db")

    populate_items("tmp/items.db")
    assert handler.search_item("Iron Pickaxe")
    assert handler.search_item("Any Balloon")
    assert handler.search_item("Abeemination")
    assert handler.search_item("Meowmere")

    os.remove("tmp/items.db")
    os.rmdir("tmp")

def test_populate_recipes_by_hand():
    test_handler = TestHandler()

    test_handler.remove_files(["tmp/items.db"])
    test_handler.remove_folders(["tmp"])

    os.mkdir("tmp")
    recipe_handler = RecipeHandler("sqlite:///tmp/items.db")

    populate_items("tmp/items.db")
    populate_recipes("by_hand", "tmp/items.db")

    assert recipe_handler.search_item(8)
    assert recipe_handler.search_item(94)
    assert recipe_handler.search_item(985)
    assert recipe_handler.search_item(73)

    os.remove("tmp/items.db")
    os.rmdir("tmp")

