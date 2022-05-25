# 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다. - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
# 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
# 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다. 

# 스택에 있는 ( 개수를 센다
# () 가 나오면 ( 개수만큼 막대가 나온다.
# ) 가 나오면 막대가 하나 나오고 ( 개수가 하나 줄어든다.

stack = []

sentence = input()
result = 0 # 총 결과
flag = True
for letter in sentence:
    
    if letter=='(':
        stack.append(letter)
        flag = True

    elif letter==')':
        if stack[-1] == '(' and flag==True:
            stack.pop()
            result = result + len(stack)
            flag = False
        
        elif flag==False:
            stack.pop()
            result = result + 1
    
    else:
        break

print(result)