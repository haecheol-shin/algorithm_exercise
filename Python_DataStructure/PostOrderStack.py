class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    
    for i in S:
        if i.isalpha():
            answer += i
            
        elif opStack.isEmpty():
            opStack.push(i)
            
        elif i == ')':
            while prec[opStack.peek()] != 1:
                answer += opStack.pop()
            
        else:
            if prec[opStack.peek()] >= prec[i]:
                answer += opStack.pop()
            opStack.push(i)

    
    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer