#!/usr/bin/env python3


import os
import sys
from collections import defaultdict 
from binaryTree import BinaryTreeCreator
from binaryTree import huffman_coding_tree

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
            if str.isalpha(i):
                if i in data :
                    data[i] = data[i] + 1
                else:
                    data[i] = 1 
        return data
    

    def parse_frequencies(self):
        data = self.create_frequency_table()
        return sorted(data.items(), key = lambda x: x[1], reverse=True)

    
if __name__ == '__main__':
    f = FileReader('input.txt')
    # print(f.create_frequency_table())
    print(f.parse_frequencies())

