n = int(input()) # 로프 개수
rope = [] # 로프가 들 수 있는 무게

for i in range(n):
    rope.append(int(input()))

rope.sort(reverse=True) # 로프 무게가 큰 순서

rope_sum = [] #  로프로 들 수 있는 최대중량

for i in range(1, n+1): # 큰 무게 X 1, 그 다음 무게 X 2 .... 가장 가벼운 무게 X n
    rope_sum.append(i*rope[i-1])

rope_sum.sort(reverse=True) # 최대중량이 큰 순서

print(rope_sum[0])