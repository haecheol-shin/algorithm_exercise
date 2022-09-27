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
                self.l.preorder_travel()
            if self.r != None:
                self.r.preorder_travel()


class Tree:

    def __init__(self, root=None):
        self.root = root


    def insert(self, key, l, r):
        if self.root == None:
            v = Node(key)
            self.root = v
        else:
            v = self.find(key, self.root)
        if v.l != None and l != None:
            left = Node(l)
            v.l = left
        
        if v.r != None and r != None:
            right = Node(r)
            v.r = right

    def find(self, item, n):
        if n.key == item:
            print(n)
            return n
        if n.l != None:
            self.find(item, n.l)
        if n.r != None:
            self.find(item, n.r)

n = int(sys.stdin.readline().rstrip())
tree = Tree()
for i in range(n):
    a, b, c = map(lambda x: None if x == '.' else x, sys.stdin.readline().rstrip().split())
    tree.insert(a, b, c)
    
tree.root.preorder_travel()