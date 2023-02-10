from pynput import keyboard
import os
from src.item_handler import ItemHandler
from src import populate_all
from src.recipe_handler import RecipeHandler

DB = "sqlite:///items.db"

def main():
    global user_input
    global running
    running = True
    while running:
        os.system("clear")
        print("""1 search resources of item
2 populate Items and Recipes
3 delete db
(q)uit""")
        with keyboard.Listener(on_press=check_input) as listener:
            listener.join()
    os.system("clear")

def check_input(key: keyboard.Key|keyboard.KeyCode|None) -> bool:
    global running
    if type(key) == keyboard.KeyCode:
        if key.char == "q":
            running = False
        if key.char in action_dict:
            action_dict[key.char]()
    elif type(key) == keyboard.Key:
        if key == keyboard.Key.esc:
            running = False
    return False

def search_resources(item_name = None):
    to_split = 0
    os.system("clear")
    item_handler = ItemHandler(DB)
    recipe_handler = RecipeHandler(DB)
    if item_name is None:
        item_name = input("What item do you want the resources of: ")
    for i in range(len(item_name)):
        if item_name[i] in "1234567890":
            to_split = i + 1
    item_name = item_name[to_split:]

    item = item_handler.search_item(item_name)

    print()
    print(get_resources(item))
    
    input("\nPress ENTER to continue")

def get_resources(item, depth=1):
    item_handler = ItemHandler(DB)
    recipe_handler = RecipeHandler(DB)

    searched = recipe_handler.search_item(item.item_id)

    to_return = f"{item.item_id}: {item.item_name}"

    if searched is None:
        return to_return
    for i in searched:
        to_return += f"\n{'  '*depth}{get_resources(item_handler.search_item_by_id(i.resource_id), depth + 1)}"
    return to_return

def populate_db():
    populate_all("items.db")

action_dict = {
    "1": search_resources,
    "2": populate_db,
    "3": lambda: os.system("rm items.db")
    }

if __name__ == "__main__":
    main()

