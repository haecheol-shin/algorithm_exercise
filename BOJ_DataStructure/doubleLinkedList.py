class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.data = data

class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = self.head

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            
        else:
            node = self.tail
            new_node = Node(data)
            node.next = new_node
            new_node.prev = self.head
            self.tail = new_node

    def __str__(self):
        node = self.head
        result = ""
        while node is not None:
            result = result + str(node.data) + " "
            node = node.next
        result = result + "이 집합의 대표원소는 " + str(self.head.data) + " 입니다."
        return result

def make_set(data):
    oneSet = DoubleLinkedList()
    oneSet.append(data)
    print(oneSet)

def find_set(Set, data):
    node = Set.head
    result = ""
    while node is not None:
        if node.data == data:
            result = str(data)+ "는 " + "대표원소가 " + str(Set.head.data) + " 인 집합에 속해있습니다."
            return result
        else:
            node = node.next
    
    result = "일치하는 원소를 가진 집합이 없습니다."
    return result

def union(Xset, Yset):
    Yset.tail.next = Xset.head

    print(Yset)

if __name__ == '__main__':
    Set1 = DoubleLinkedList()
    Set1.append(1); Set1.append(2); Set1.append(3)
    
    Set2 = DoubleLinkedList()
    Set2.append(4); Set2.append(5); Set2.append(6); Set2.append(7); Set2.append(8)

    print(Set1)
    print()
    print(Set2)
    print()
    
    make_set(100)
    print()

    print(find_set(Set1, 3))
    print()
    
    union(Set1, Set2)
    print()