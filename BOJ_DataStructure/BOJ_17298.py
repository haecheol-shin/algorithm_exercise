import sys

n = int(sys.stdin.readline()) # 수열의 크기
intSequence = list(map(int, input().split()))
result = []

for i in range(n):
    for j in range(i+1, n):
        if (intSequence[i]<intSequence[j]):
            result.append(intSequence[j])
            break

        if (j==n-1):
            result.append(-1)
            break

result.append(-1)

print(result)