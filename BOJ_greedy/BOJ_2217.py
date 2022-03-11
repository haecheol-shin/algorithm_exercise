n = int(input()) # 로프 개수
rope = [] # 로프가 들 수 있는 무게

for i in range(n):
    rope.append(int(input()))

min = 10000 # 가장 약한 로프
for i in range(n):
    if (min>rope[i]):
        min = rope[i]

print(min*n)
