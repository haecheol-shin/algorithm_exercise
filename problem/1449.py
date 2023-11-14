import sys

N, L = map(int, sys.stdin.readline().split())
locations = list(map(int, sys.stdin.readline().split())) # string->int

# 오름차순으로 for문 돌림
# (배열에 들어있는 숫자)랑 (그 전 배열+테이프 길이) 비교
# 같으면 테이프 붙히고 테이프 길이만큼 더함
# 적으면 넘어감
# 크면 그 숫자가 다시 기준 + 테이프 붙힘

locations.sort()

k = 1 # 비교할 숫자
answer = 0
for location in locations:
    if k == location:
        answer += 1
        k += L

    elif k > location:
        continue

    else:
        k = location + L
        answer += 1

print(answer)