n = int(input()) # 회의 총 개수

meeting_list = [0 for i in range(n*2)]

result = 0 # 결과 값

min_finish = 2**31-1 # 가장 빨리 끝나는 회의 시간

for i in range(n):
    meeting_list[i*2], meeting_list[i*2+1] = map(int, input().split()) # 짝수번에 시작시간, 홀수번에 끝나는 시간

while(True):
    for i in range(1, len(meeting_list), 2): # 회의 중 가장 빨리 끝나는 시간을 찾음
        if (min_finish > meeting_list[i]):
            min_finish = meeting_list[i]

    result += 1 # 결과 값 1 증가

    for i in range(0, len(meeting_list)-1, 2): # 가장 빨리 끝나는 시간보다 회의 시작 시간이 작으면 삭제
        if (min_finish > meeting_list[i]):
            del meeting_list[i]
            del meeting_list[i+1] # 리스트 길이가 줄어 인덱스 범위 오류 해결X

    if (len(meeting_list)<=1):
        break

print(result)

