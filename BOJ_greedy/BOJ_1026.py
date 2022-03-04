n = int(input()) # 배열의 길이가 n

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

max_b = 0 # b의 최댓값
sum = 0 # 결과

while(len(a)!=0):
    for i in range(len(b)): # b배열에서 가장 큰 값 찾기
        if (max_b<b[i]):
            max_b = b[i]

    sum = sum + max_b*a[0] # a의 푀솟값과 b의 최댓값을 곱해서 더해줌

    del a[0] # a의 최솟값 삭제
    
    for i in range(len(b)):
        if (max_b==b[i]):
            del b[i] # b의 최댓값 삭제
            break # 같은 값이 여러개일 경우를 대비해 한번만 삭제하게 만듬

    max_b = 0 # b최댓값 초기화
    
print(sum)

##############최적코드###############

# n = int(input())

# a_list = list(map(int, input().split()))
# b_list = list(map(int, input().split()))

# s = 0
# for i in range(n):
#     s += min(a_list) * max(b_list)
#     a_list.pop(a_list.index(min(a_list)))
#     b_list.pop(b_list.index(max(b_list)))

# print(s)