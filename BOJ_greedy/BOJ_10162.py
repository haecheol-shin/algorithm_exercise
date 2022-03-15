t = int(input()) # 총 시간

a = 5 * 60 # 5분 * 60초
b = 1 * 60 # 1분 * 60초
c = 10 # 10초

a_cnt = 0 # a를 누른 횟수
b_cnt = 0
c_cnt = 0
temp = 0 # 나머지
if (t%10!=0):
    print(-1)

else:
    a_cnt = t // a
    temp = t % a

    b_cnt = temp // b
    temp = temp % b

    c_cnt = temp // c

    print(a_cnt, b_cnt, c_cnt)
