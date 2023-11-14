import sys

N, K = map(int, sys.stdin.readline().split())

coinType = []
for _ in range(N):
    coinType.append(int(sys.stdin.readline()))

# 위의 라인 세 줄은
# coinType = [int(sys.stdin.readline()) for _ in range(N)]
# 으로 바꿔 쓸 수 있다.

coinType.sort(reverse=True)
result = 0
for coin in coinType:
    result += (K // coin)
    K = K % coin

print(result)