import sys

n = int(sys.stdin.readline())
arr = [i for i in range(1, n+1)] # 1부터 시작되는 오름차순 리스트 생성
inputSequence = [] # 수열을 입력받을 리스트 
result = [] # 결과 값을 저장하는 리스트

for i in range(n):
    inputSequence.append(int(sys.stdin.readline()))

index = -1
for i in range(n):
    index = inputSequence[i] - (i+1)

