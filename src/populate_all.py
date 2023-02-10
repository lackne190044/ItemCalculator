from src import populate_items
from src import populate_recipes


def populate_all(db: str):
    populate_items(db)
    populate_recipes("by_hand", db)
    populate_recipes("furnace", db)
    populate_recipes("iron_lead_anvil", db)
    populate_recipes("mythril_orichalcum_anvil", db)
    populate_recipes("crimson_demon_altar", db)

if __name__ == "__main__":
    populate_all("items.db")

