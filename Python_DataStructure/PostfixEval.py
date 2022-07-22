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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)

        elif opStack.isEmpty() or token == '(':
            opStack.push(token)

        elif token == ')':
            while prec[opStack.peek()] != 1:
                postfixList.append(opStack.pop())
            opStack.pop()

        else:
            for _ in range(2):
                if prec[opStack.peek()] >= prec[token]:
                    postfixList.append(opStack.pop())
                if opStack.isEmpty() or opStack.peek() == '(':
                    break
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return postfixList


def postfixEval(tokenList):
    val = ArrayStack()
    for token in tokenList:
        if type(token) is int:
            val.push(token)
        
        else:
            second = val.pop()
            first = val.pop()

            if token == '+':
                val.push(first+second)

            elif token == '-':
                val.push(first-second)

            elif token == '*':
                val.push(first*second)

            else:
                val.push(first/second)
    
    return val.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

if __name__=="__main__":
    a = "5 + 3"
    print(solution(a))