n = int(input()) # 배달해야하는 무게
t = int(0) # 3킬로 봉지
f = int(0) # t는 3킬로 봉지

f = n//5 # 5킬로그램 봉지 개수는 n을 5로 나눈 몫

remains = n%5 # 5킬로그램으로 나눈 나머지

if (remains==0): # 나머지가 0일때
    print(f)

elif (remains==1): # 나머지가 1일때
    if(f==0):
        print(-1) # 무게가 1킬로면 성립X
    
    else:
        f -= 1
        t = 2
        print(f+t) # 5킬로봉지를 1개 줄이고 3킬로 봉지를 두개 늘림

elif (remains==2): # 나머지가 2일때
    if (f<2):
        print(-1) # 무게가 12킬로를 넘지 않는다면 성립X

    else:
        f -= 2
        t = 4
        print(f+t) # 5킬로 봉지 2개 줄이고 3킬로 봉지 4개 늘림

elif (remains==3): # 나머지가 3일때
    t = 1
    print(f+t) # 3킬로봉지 1개

else: # 나머지가 4일때
    if (f==0):
        print(-1) #무게가 4킬로면 성립X
    
    else:
        f -= 1
        t = 3
        print(f+t) #5킬로봉지 1개 줄이고 3킬로 봉지 3개 늘림