from src.item_handler import ItemHandler
from src.model import Item


def populate_items(location):
    handler = ItemHandler(f"sqlite:///{location}")

    with open('src/Data/items.txt', 'r') as f:
        data = f.readlines()

    objects = []

    count = 0
    for i in data:
        i = i.replace("\t", "")
        count += 1
        name = ' '.join(i.split(' ')[1:-1])
        objects.append(Item(item_name=name))

    handler.bulk_add_to_db(objects)
    
if __name__ == "__main__":
    populate_items("items.db")

