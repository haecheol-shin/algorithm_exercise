from time import time


n = int(input()) # 사람 수

time_list = list(map(int, input().split())) # 리스트에 각 사람이 걸리는 시간을 넣음

time_list.sort(reverse=True) # 내림차순으로 정렬

sum = 0 # 시간 합계

for i in range(n):
    sum = sum + time_list[i] * (i+1) # 가장 작은 숫자는 n번, 다음 숫자는 n-1번... 마지막은 1번 곱해져서 총 합이 구해짐

print(sum)


