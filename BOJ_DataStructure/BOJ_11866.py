n, k = map(int, input().split())

result = []
num = [ i for i in range(1, n+1)]

index = 0
while(len(num)!=0):
    index += k-1
    while(index >= len(num)): # while 문으로 index값을 설정해야한다.
        index -= len(num)
    
    result.append(num.pop(index))

print("<"+str(result)[1:-1]+">") # 리스트 출력 시 대괄호 지우는 방법
