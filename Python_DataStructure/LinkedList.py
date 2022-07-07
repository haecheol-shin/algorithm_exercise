class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos): # 특정 노드를 참조하는 메소드
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head # 처음에 head를 넣어줌
        while i < pos:
            curr = curr.next # 다음 노드를 가리킴
            i += 1
        return curr

    def traverse(self): # getAt 메소드를 사용하면 처음 방문했던 노드도 계속해서 방문하기 때문에 사용하면 안된다.
        answer = []
        i = 1
        curr = self.head
        while i <= self.nodeCount:
            answer.append(curr.data)
            curr = curr.next
            i += 1
        return answer


# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0