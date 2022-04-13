import sys

n = int(sys.stdin.readline())
inputSequence = [] # 수열을 입력받을 리스트 
result = [] # 결과 값을 저장하는 리스트

for i in range(n):
    inputSequence.append(int(sys.stdin.readline()))

pushCount = 0 # 수열이 반복문을 돌아가면서 가장 높은 수를 저장
plusCount = 0 # +를 몇번 찍어야하는지 저장하는 변수

for i in range(n):
    if (i==0 or inputSequence[i-1]-inputSequence[i]<=1):
        pass
    
    else:
        print("NO")
        break
    
    if (inputSequence[i]>pushCount):
        pushCount = inputSequence[i] # 가장 높은 수를 저장
        plusCount = pushCount - plusCount # 가장 높은 수 - 이미 저장된 +개수
        for j in range(plusCount):
            result.append('+')
    
    result.append('-')

    if (i==n-1):
        for j in range(len(result)):
            print(result[j])

    else:
        pass

#######################################
import sys

n = int(sys.stdin.readline())
inputSequence = [] # 수열을 입력받을 리스트
arr = [i for i in range(1,n+1)]
emptyArr = [0 for ]
result = [] # 결과 값을 저장하는 리스트

for i in range(n):
    inputSequence.append(int(sys.stdin.readline()))

for i in range(n):

    
for i in range(len(result)):
    print(result[i])