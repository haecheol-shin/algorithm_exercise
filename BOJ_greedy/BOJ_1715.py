n = int(input()) # 카드 뭉치 개수
card_cnt = []

for i in range(n):
    card_cnt.append(int(input()))

# 3개의 뭉치 10 20 40 최솟값은 100
# 10+20 / 30+40 --> 10이 2번 20이 두번 40이 1번
# 5개의 뭉치 10 20 30 40 50
# 10+20 / 30+30 / 60+40 / 100+50
# 30+60+100+150 = (10+20)+(10+20+30)+(10+20+30+40)+(10+20+30+40+50)

#가장 낮은 숫자와 두번째 낮은 숫자가 N-1번 곱해지고 순차적으로 1씩 줄어든다

sum = 0
card_cnt.sort()

for i in range(n):
    if (i==0 or i==1):
        sum += card_cnt[i] * (n-1)
    
    else:
        sum += card_cnt[i] * (n-i)

print(sum)