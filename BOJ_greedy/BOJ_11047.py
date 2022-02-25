n, k = map(int, input().split()) # n은 값어치 종류, k는 총합

value_list = [] # 동전 값어치를 리스트로 저장

for i in range(n):
    value_list.append(int(input()))

value_list.sort(reverse=True) # 값어치 내림차순 정렬

sum = 0 # 동전 총 개수
remain = 0 # 나머지

for i in range(n):
    sum = sum + (k//value_list[i])
    k = k%value_list[i]

print(sum)