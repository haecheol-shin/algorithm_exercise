from collections import Counter

n = int(input()) # 개수
data = list(map(int, input().split())) # 숫자를 리스트 형태로 저장
count = Counter(data) # 변수 마다 중복 횟수를 저장
stack = []
result = [-1] * n # 결과를 -1로 초기화
stack.append(0)

for i in range(n):
    while stack and count[data[stack[-1]]] < count[data[i]]:
        result[stack.pop()] = data[i]
    stack.append(i)

for r in result:
    print(r, end=' ')