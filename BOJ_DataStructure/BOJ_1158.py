import sys

userInput = sys.stdin.readline().split()
n = int(userInput[0])
k = int(userInput[1])
intArr = [i for i in range(1,n+1)] # 1,2,3,4,5,6,....배열
Josephus = []
pointer = 0 # 포인터 역할을 하는 변수 선언
for i in range(n):
    pointer += (k-1) # k-1만큼 포인터가 증가
    while(pointer>=len(intArr)): # 포인터의 크기가 배열보다 크면 안된다
        pointer -= len(intArr)

    
    Josephus.append(intArr.pop(pointer))

print('<'+str(Josephus)[1:-1:]+'>')