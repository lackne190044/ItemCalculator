import os
from src import item_handler
from src import populate_all

class TestHandler:
    def remove_files(self, files: list):
        for i in files:
            if os.path.exists(i):
                os.remove(i)

    def remove_folders(self, folders: list):
        for i in folders:
            if os.path.exists(i):
                os.rmdir(i)

    def populate(self):
        populate_all("tmp/items.db")

