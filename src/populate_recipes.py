import sys

from src.item_handler import ItemHandler
from src.recipe_handler import RecipeHandler
from src.model import Recipe


def remove_duplicate(duplicate_name: list):
    if len(duplicate_name) > 1:
        return " ".join(duplicate_name[:int(len(duplicate_name)/2)]) + " " + duplicate_name[-1]
    return duplicate_name[0][:int(len(duplicate_name[0])/2)]

def populate_recipes(file, location):
    item_handler = ItemHandler(f"sqlite:///{location}")
    recipe_handler = RecipeHandler(f"sqlite:///{location}")

    recipes = []

    with open("src/Data/" + file + ".txt", 'r') as f:
        data = f.readlines()

    i = 0

    while i < len(data):
        white_space = True
        needed = []

        duplicate_item = data[i]
        duplicate_item = data[i].split()

        if ')' in duplicate_item[-1] and duplicate_item[-1][1] in "0123456789":
            duplicate_item.pop()[1:-1]

        duplicate_item = remove_duplicate(duplicate_item)

        item = item_handler.search_item(duplicate_item)
        i += 1
        while white_space and i < len(data):
            amount = 1
            current_data = data[i]

            if current_data[0] != " " and current_data != "\n":
                white_space = False
                i -= 1

            current_data = current_data.replace("\n", "")
            current_data = current_data.replace("\t", "")

            current_data = current_data.split()

            if current_data != []:
                if ')' in current_data[-1] and current_data[-1][1] in "0123456789":
                    amount = current_data.pop()[1:-1]

                current_data = remove_duplicate(current_data)

            if current_data != [] and white_space:
                needed.append((current_data, amount))

            i += 1


        for resource, amount in needed:
            recipes.append(Recipe(item_id=item.item_id, resource_id=item_handler.search_item(resource).item_id, resource_amount=amount))
    recipe_handler.bulk_add_to_db(recipes)


if __name__ == "__main__":
    # populate_recipes(sys.argv[1], "items.db")
    populate_recipes("mythril_orichalcum_anvil", "items.db")

