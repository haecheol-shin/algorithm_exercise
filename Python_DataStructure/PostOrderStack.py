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

def solution(S): # 중위 연산식을 후위 연산식으로 바꾸는 함수 ( 소괄호만 적용, 식의 유효성 검사는 안함)
    opStack = ArrayStack()
    answer = ''
    
    for i in S:
        if i.isalpha(): # 피연산자는 무조건 출력
            answer += i
            
        elif opStack.isEmpty() or i == '(': # 비어있거나 여는 괄호는 무조건 스택에 push
            opStack.push(i)
            
        elif i == ')': # 닫는 괄호가 나올 경우 짝이 맞는 여는 괄호가 나올 때 까지 스택을 pop
            while prec[opStack.peek()] != 1:
                answer += opStack.pop()
            opStack.pop()
            
        else:
            for _ in range(2): # 반복문을 두번만 돌림 -> 스택에서 pop을 해도 스택 맨위의 연산자가 현재 연산자보다 우선순위가 높은 경우는 최대 두번이 끝이다.
                if prec[opStack.peek()] >= prec[i]:
                    answer += opStack.pop()
                if opStack.isEmpty() or opStack.peek() == '(': # pop을 했을 때 다음 스택의 맨 위에 ( 가 나오거나 빈 스택이 되면 break 해야한다.
                    break
            opStack.push(i)

    
    while not opStack.isEmpty(): # 식을 다 읽고나서 스택에 연산자가 남아있는 경우 전부 pop해준다.
        answer += opStack.pop()

    return answer