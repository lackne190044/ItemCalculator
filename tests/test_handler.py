import os

class TestHandler:
    def remove_files(self, files: list):
        for i in files:
            if os.path.exists(i):
                os.remove(i)

    def remove_folders(self, folders: list):
        for i in folders:
            if os.path.exists(i):
                os.rmdir(i)

