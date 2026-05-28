import os

class FileManager():
    def __init__(self, path):
        self.path = path

    def read_file(self):
        if os.path.exists(self.path):
            with open(self.path) as f:
                return f.read()
        else:
            raise Exception("Data file not found.")

    def write_file(self, text=''):
        with open (self.path, 'w') as f:
            f.write(text)