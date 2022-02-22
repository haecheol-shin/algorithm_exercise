n = int(input()) # 배달해야하는 무게
t,f = 0 # t는 3킬로 봉지, f는 5킬로 봉지

f = n//5 # 5킬로그램 봉지 개수는 n을 5로 나눈 몫

remains = n%5 # 5킬로그램으로 나눈 나머지

if (remains==0):
    print(f)

elif (remains==1):
    f -= 1
    t = 2
    print(f+t)

elif (remains==2):
    if