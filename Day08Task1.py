import sys

sys.setrecursionlimit(10000) 
# I use recursion here because it makes the neatest code (I think), 
# but Python does not have Tail Call Optimization so if the input were much larger, 
# I might run out of memory and get a stack overflow

class Node: 
    
    def __init__(self, n_children, n_metadata, children, metadata):

        self.header = [n_children, n_metadata]
        self.children = children
        self.metadata = metadata


def getMetadataSum(tree):

    if tree.header[0] == 0:
        return sum(tree.metadata)
    else:
        result = sum(tree.metadata)    
        for child in tree.children:
            result += getMetadataSum(child)

        return result

def parseNodeList(data, n_nodes, start_index):
    n_left_to_parse = n_nodes
    node_list = []
    i = start_index # index of number I am parsing
    while n_left_to_parse > 0:

        n_children = data[0 + i]
        n_metadata = data[1 + i]
        
        if n_children == 0:
            children = []
            metadata = data[2 + i : 2 + i + n_metadata]
            i = 2 + i + n_metadata
            n_left_to_parse -= 1
        else:
            children, j = parseNodeList(data, n_children, i + 2)
            metadata = data[j : j+n_metadata]
            i = j + n_metadata
            n_left_to_parse -= 1
        
        node_list.append(Node(n_children, n_metadata, children, metadata))

    return node_list, i 

with open("/Users/DominikKloepfer/Documents/workspace/Personal_Projects/Advent of Code 2018/Day 8/day8_input1.txt") as input: 
    data = [line.strip().split(' ') for line in input]
    data = [int(number) for number in data[0]]

tree, i = parseNodeList(data, 1, 0)

print(getMetadataSum(tree[0]))