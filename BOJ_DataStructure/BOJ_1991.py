import sys
from turtle import right

class Node():
    def __init__(self, key):
        self.key = key
        self.l = None
        self.r = None

class Tree:

    def __init__(self, root):
        self.root = root

    def insert(self, key, l, r):
        node = Node(key)
        if self.root == None:
            self.root = node
        left = Node(l)
        right = Node(r)
        node.l = left
        node.r = right

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    nodeInput = list(sys.stdin.readline().rstrip().split())
    node = Node(nodeInput[0])
    
