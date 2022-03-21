# 정답은 맞으나 시간초과 문제발생 -> 아무래도 이중 for문을 쓰면 안되는듯

n = int(input()) # 도시 개수
distance = list(map(int, input().split())) # 도시 사이 거리
price = list(map(int, input().split())) # 리터 당 가격
sum = 0 # 가격 총합
k = 0 # for문에 필요한 변수

for i in range(n-1):
    sum += price[i] * distance[i]

    for j in range(i, len(distance)): # 현재 주유소 가격이 다음가격보다 싸면 다음거리만큼 이번주유소에서 충전을 한다
        k = j+1
        if (price[i]<price[k]):
            sum += price[i] * distance[k]
            distance[k] = 0

print(sum)
   


    
