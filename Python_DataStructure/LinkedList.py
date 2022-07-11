class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount: # 삭제하려는 원소의 위치가 인덱스 범위를 벗어난 경우
            raise IndexError("IndexError")
        
        if self.head == self.tail: # 삭제하려는 원소가 리스트 내에서 유일한 원소인 경우
            curr = self.head
            self.head = None # head 조정
            self.tail = None # tail 조정
        # 따로 처리해야 하는 이유는 head와 tail 조정이 둘다 이뤄져야 하기 때문
        
        elif pos == 1: # 삭제하려는 원소의 위치가 맨 앞인 경으
            curr = self.head
            self.head = self.head.next # head 조정
            curr.next = None
        
        elif pos == self.nodeCount: # 삭제하려는 원소의 위치가 맨 뒤인 경우
            prev = self.getAt(pos-1)
            curr = prev.next
            self.tail = prev # tail 조정
            prev.next = None
            
        else: # 삭제하려는 원소의 위치가 중간인 경우
            prev = self.getAt(pos-1)
            curr = prev.next
            prev.next = curr.next
            curr.next = None
        
        self.nodeCount -= 1
        return curr.data


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0


