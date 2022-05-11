import sys

n = int(sys.stdin.readline()) # 피연산자 개수
stack = [] # 피연산자를 저장할 스택
sentence = sys.stdin.readline() # 후위 표기식
num = [] # 피연산자의 숫자를 저장하는 배열

for i in range(n):
    num.append(sys.stdin.readline())
    if sentence[i]=='+' or sentence[i]=='-' or sentence[i]=='*' or sentence[i]=='/':
        pass

    else:    
        sentence.replace(num[i], sentence[i])

print(sentence)
print(sentence[0])


# for i in range(n):
#     stack[i] = sentence[i]

#     if (i>=2):
#         if(type(sentence[i-2])==int and type(sentence[i-1])==int and type(sentence[i-2])==str):
#             sentence[i-2]