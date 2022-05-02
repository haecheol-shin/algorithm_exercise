# <>안에 있는 단어는 큐로 출력
# 그냥 단어는 스택으로 출력
# 단어는 공백으로 구분하되, 단어안에 있는 공백은 단어취급

import sys
from collections import deque

sentence = sys.stdin.readline()

result = ''
stack = []
queue = deque([])

for i in sentence:
    print(i)