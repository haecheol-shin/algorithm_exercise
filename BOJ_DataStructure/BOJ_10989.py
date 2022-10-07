import sys 

n = int(sys.stdin.readline())

numCountList = [0] * 10000

for i in range(n):
    num = int(sys.stdin.readline())
    numCountList[num-1] += 1

for i in range(n):
    # 출력을 숫자 개수만큼 반복해서 찍는데
    # 값이 0인 인덱스는 그냥 지나가야함
