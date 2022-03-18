n = int(input()) # 자연수가 주어짐

result = 0 # 결과 값

cnt = 0 # n에서 뺄 값

while(True):
    cnt += 1 # 반복문이 돌때마다 1 증가
    n -= cnt
    
    if (n<=cnt): # 남은 수가 뺄 수보다 작거나 같다면
        result += 1
        break
    
    result += 1

print(result)