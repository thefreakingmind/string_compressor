import os
import sys
from collections import defaultdict 
from binaryTree import BinaryTreeCreator


class FileReader(object):
    def __init__(self, filename):
        self.filename = filename
        
    
    def process_file(self):
        with open(self.filename, 'r') as f: 
            if f is None:
                print("Error in reading File")
                return 
            return f.read()

    # Take the String and create a frequency map 
    def create_frequency_table(self):
        data = {}
        for i in self.process_file():
            if i in data:
                data[i] = data[i] + 1
            else:
                data[i] = 1 
        return data
    
    
if __name__ == '__main__':
    f = FileReader('input.txt')
    print(f.create_frequency_table())
