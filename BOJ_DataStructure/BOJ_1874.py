import sys

n = int(sys.stdin.readline()) # 수열의 길이를 입력받음
inputSequence = [] # 수열을 입력받을 리스트 
result = [] # 결과 값을 저장하는 리스트
stack = [] # 스택

for i in range(n):
    inputSequence.append(int(sys.stdin.readline())) # 수열을 입력받음

top = 0 # 아래 반복문을 반복하면서 나온 수 중 가장 큰 수
for i in range(n):
    if (inputSequence[i]>top): # 현재 수가 top보가 클 때
        for j in range(top+1,inputSequence[i]+1): # top+1부터 현재 수 까지 스택에 수를 집어넣음
            stack.append(j)
            result.append('+') # 반복문이 돌아간만큼 +를 넣어줌
        top = inputSequence[i] # top를 바꿔줌
    
    if (inputSequence[i]!=stack.pop()): # 만약 pop을 했는데 현재 수와 다른 경우
        print("NO") # 불가능한 수열
        break
    result.append('-') # 반복문 가장 마지막에 -를 넣어줌

    if (i==n-1): # 반복문이 다 돌아갔다면
        for j in result: # 결과출력
            print(j)




