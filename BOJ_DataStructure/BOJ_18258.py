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
            self.nodeCount += 1
        
        else:  # tail에서 들어가도록 바꿔야함.
            curr = self.tail.prev
            curr.next = newNode
            self.tail.prev = newNode
            newNode.next = self.tail
            newNode.prev = curr
            self.nodeCount += 1

    def pop(self):
        if self.nodeCount == 0:
            return -1

        else:
            curr = self.head.next
            self.head.next = curr.next
            curr.next.prev = self.head
            self.nodeCount -= 1
            return curr.data

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
        command = sys.stdin.readline().split()

        if command[0]=='push':
            queue.push(int(command[1]))

        elif command[0]=='pop':
            result = queue.pop()
            sys.stdout.write(str(result)+'\n')

        elif command[0]=='size':
            result = queue.size()
            sys.stdout.write(str(result)+'\n')

        elif command[0]=='empty':
            result = queue.empty()
            sys.stdout.write(str(result)+'\n')

        elif command[0]=='front':
            result = queue.front()
            sys.stdout.write(str(result)+'\n')

        else:
            result = queue.back()
            sys.stdout.write(str(result)+'\n')

# 클래스로 구현해서 시간초과 뜨는 듯