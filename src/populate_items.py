from db_handler import DB_Handler
from model import Item

handler = DB_Handler("sqlite:///items.db")

with open('Data/items.txt', 'r') as f:
    data = f.readlines()


objects = []

count = 0
for i in data:
    count += 1
    name = ' '.join(i.split(' ')[1:-1])
    objects.append(Item(item_name=name))

handler.bulk_add_to_db(objects)
    
