import sys

class Node():
    def __init__(self, key):
        self.key = key
        self.l = None
        self.r = None

    def preorder_travel(self):
        if self:
            sys.stdout.write(self.key)
            if self.l != None:
                print('d')
                self.l.preorder_travel()
            if self.r != None:
                print('b')
                self.r.preorder_travel()


class Tree:

    def __init__(self, root=None):
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
tree = Tree()
for i in range(n):
    a, b, c = map(lambda x: None if x == '.' else x, sys.stdin.readline().rstrip().split())
    tree.insert(a, b, c)
    
tree.root.preorder_travel()