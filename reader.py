import os
import sys

class FileReader(object):
    def __init__(self, filename):
        self.filename = filename
    
    def process_file(self):
        with open(self.filename, 'r') as f: 
            if f is None:
                print("Error in reading File")
                return
            return f.read()

    def process_node_name(self):
        pass


if __name__ == '__main__':
    f = FileReader('input.txt')
    print(f.process_file())
