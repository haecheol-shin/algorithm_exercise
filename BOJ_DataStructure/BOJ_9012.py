# 성립조건
# 1. 여는괄호 개수 == 닫는 괄호 개수
# 2. 닫는 괄호 개수가 한번이라도 여는 괄호 개수를 초과하면 안된다.

import sys

n = int(sys.stdin.readline()) # 테스트 개수

for i in range(n):
    parenthesisStr = sys.stdin.readline()
    
    lParenthesis = int(0) # 여는 괄호의 개수
    rParenthesis = int(0) # 닫는 괄호의 개수
    for j in range(len(parenthesisStr)): # 문장 길이 만큼 반복
        if (parenthesisStr[j]=='('):
            lParenthesis += 1

        elif (parenthesisStr[j]==')'):
            rParenthesis += 1

        if (lParenthesis<rParenthesis): # 닫는 괄호의 개수가 한번이라도 더 많으면 NO
            print("NO")
            break

        else:
            pass

        if (j==len(parenthesisStr)-1): # 반복문이 다 돌았을 때
            if (lParenthesis==rParenthesis): # 여는 괄호 개수와 닫는 괄호 개수가 다르면 NO
                print("YES")
            
            else:
                print("NO")