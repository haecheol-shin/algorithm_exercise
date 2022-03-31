n = int(input()) # 카드 뭉치 개수
card_cnt = []

for i in range(n):
    card_cnt.append(int(input()))

# 3개의 뭉치 10 20 40 최솟값은 100
# 10+20 / 30+40 --> 10이 2번 20이 두번 40이 1번
# 먼저 최대한 작은 숫자들끼리 뭉친다
# 그 다음 숫자들끼리 뭉친다
# 홀수가 남았을 경우 가장 큰 숫자를 남긴다

sum = 0
while(True):

    if (len(card_cnt)%2==0): # 카드 수가 짝수 일 경우
        for i in range(0,len(card_cnt),2):
            addNum = card_cnt[i] + card_cnt[i+1]
            card_cnt[i] = addNum
            card_cnt[i+1] = addNum

    else: # 카드 수가 홀수 일 경우 마지막 카드를 그대로 놔두기위해 반복문 길이를 하나 줄임
        for i in range(0,len(card_cnt)-1,2):
            addNum = card_cnt[i] + card_cnt[i+1]
            card_cnt[i] = addNum
            card_cnt[i+1] = addNum # 뭉친 숫자를 더했던 공간에 똑같은 숫자를 넣어줌

    for j in range(len(card_cnt)): # 홀수 인덱스인 곳은 요소를 0으로 바꿈
        if (j%2==1):
            sum += card_cnt[j]
            card_cnt[j] = 0
    
    card_cnt.sort() # 오름차순 정렬
    card_cnt = card_cnt[int(len(card_cnt)/2):] # 요소가 0인 부분은 삭제

    if (len(card_cnt)==1):
        break

print(sum)