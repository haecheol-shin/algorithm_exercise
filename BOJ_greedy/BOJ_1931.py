# n = int(input()) # 회의 총 개수

# meeting_list = [0 for i in range(n*2)]

# result = 0 # 결과 값

# min_finish = 2**31-1 # 가장 빨리 끝나는 회의 시간

# break_num = 1

# for i in range(n):
#     meeting_list[i*2], meeting_list[i*2+1] = map(int, input().split()) # 짝수번에 시작시간, 홀수번에 끝나는 시간

# while(break_num!=0):
#     for i in range(1, len(meeting_list), 2): # 회의 중 가장 빨리 끝나는 시간을 찾음
#         if (min_finish > meeting_list[i]):
#             min_finish = meeting_list[i]

#     result += 1 # 결과 값 1 증가

#     for i in range(0, len(meeting_list), 2): # 가장 빨리 끝나는 시간보다 회의 시작 시간이 작으면 삭제
#         if (min_finish > meeting_list[i]):
#             meeting_list[i] = 2**31-1
#             meeting_list[i+1] = 2**31-1

#     min_finish = 2**31-1

#     for i in range(len(meeting_list)):
#         if (meeting_list[i] != 2**31-1):
#             break

#         if (i==len(meeting_list)-1):
#             break_num = 0

# print(result)

n = int(input())
time = []

for _ in range(n):
  start, end = map(int, input().split())
  time.append([start, end])

time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순

last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in time:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j

print(conut)