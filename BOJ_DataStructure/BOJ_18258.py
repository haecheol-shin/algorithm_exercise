# push, pop, size, empty, front, back
# 모두 O(1)이 걸려야 함
# 이중연결리스트로 구현한 queue를 써야 할 듯

import sys

class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Queue:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def push(self, X):
        newNode = Node(X)
        if self.nodeCount == 0:
            self.head.next = newNode
            self.tail.prev = newNode
        
        else:
            curr = self.head.next
            self.head.next = newNode
            curr.prev = newNode
        

    def size(self):
        return self.nodeCount

    def empty(self):
        if self.nodeCount == 0:
            return 1

        else:
            return 0

    def front(self):
        if self.nodeCount == 0:
            return -1

        else:
            return self.head.next.data

    def back(self):
        if self.nodeCount == 0:
            return -1

        else:
            return self.tail.prev.data


if __name__=="__main__":
    n = int(sys.stdin.readline())
    queue = Queue()
    for i in range(n):
        command = list(sys.stdin.readline().split())

        if command[0]=='push':

        elif command[0]=='pop':

        elif command[0]=='size':

        elif command[0]=='empty':

        elif command[0]=='front':

        else:


