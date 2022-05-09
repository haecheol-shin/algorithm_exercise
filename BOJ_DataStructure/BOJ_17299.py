# 앞에서부터 계산하며
# 변수 변수 연산자가 되면 계산한다

import sys

n = int(sys.stdin.readline()) # 피연산자 개수

sentence = sys.stdin.readline() # 수식
operand = []

for i in range(n):
