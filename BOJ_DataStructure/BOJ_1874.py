# 조건: 들어가있는 숫자보다 출력하려는 숫자가 크면 안된다
# 출력하려는 숫자를 출력하기 위해서 부족한 숫자만큼 push
# pop을 하면 top에 있는 숫자가 하나빠짐
# push횟수: 4 pop횟수: 0 출력가능한 최대숫자: 4
# --> if(출력숫자<=push횟수-pop횟수) 이면 출력 가능
# else: 출력불가능 print("NO")

import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

for i in range(n):
    for j in range()