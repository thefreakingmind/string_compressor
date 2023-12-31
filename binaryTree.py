# This is to create a binary tree for making our compressor in python 

# Implement the compression algorithm for compressing the string
class BinaryTreeCreator(object):
    def __init__(self, right, left):
        self.right = right 
        self.left = left

    def children(self):
        return (self.left, self.right)
        
    def node(self):
        return (self.left, self.right)
        

    def __str__(self):
        return f"{self.right} + '''_'''+ {self.left}"
    
    def check_for_node(self):
        pass


def huffman_coding_tree(node, left=True, binString= ''):
    if type(node) is str:
        return {node: binString}
    
    (l, r) = node.children() 
    d = dict() 
    d.update(huffman_coding_tree(l, True, binString + '0'))
    d.update(huffman_coding_tree(l, False, binString + '0'))
    return d

            