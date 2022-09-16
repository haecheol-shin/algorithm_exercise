import sys

class Node:

    def __init__(self, item):
        self.data = item
        self.right = None
        self.left = None

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1


class Tree:

    def __init__(self, root):
        self.root = root

    def insert(self, node):
        if self.nodeCount==0:
            self.root = node
        
        else:



if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())

    for i in range(n):
        node = sys.stdin.readline().rstrip().split()
        # node[0] -> data
        # node[1] -> left
        # node[2] -> right