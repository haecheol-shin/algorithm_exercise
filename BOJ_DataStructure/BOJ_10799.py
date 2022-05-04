# <>안에 있는 단어는 큐로 출력
# 그냥 단어는 스택으로 출력
# 단어는 공백으로 구분하되, 단어안에 있는 공백은 단어취급

import sys
from collections import deque

sentence = sys.stdin.readline()

result = '' # 결과를 저장
queue = deque([]) # 단어를 저장할 데크
temp = [] # 단어를 임시로 저장함
signal = False

for i in sentence:
    if (signal == True):

        if (i=='>'):
            queue.append(i)
            for i in range(len(queue)):
                result.join(queue.popleft())
            result.join(' ')
            signal = False

        else:
            queue.append(i)
    else:
        if (i=='<'):
            queue.append(i)
            signal = True

        elif (i==' '):
            result.join(queue.pop())
            result.join(' ')
        else:
            queue.append(i)    

print(result)