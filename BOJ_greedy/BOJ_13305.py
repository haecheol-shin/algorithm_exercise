n = int(input()) # 도시 개수
distance = list(map(int, input().split())) # 도시 사이 거리
price = list(map(int, input().split())) # 리터 당 가격
sum = 0 # 가격 총합
now_price = price[0] # 현재 곱하는 가격

for i in range(n-1):
    sum += now_price * distance[i]
    
    if (now_price>price[i+1]):
        now_price = price[i+1]

print(sum)
