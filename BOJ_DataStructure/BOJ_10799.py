# <>안에 있는 단어는 큐로 출력
# 그냥 단어는 스택으로 출력
# 단어는 공백으로 구분하되, 단어안에 있는 공백은 단어취급

import sys
from collections import deque

sentence = sys.stdin.readline()

result = '' # 결과를 저장
queue = deque([]) # 단어를 저장할 데크

for i in sentence:
    if (i=='<'):
        # > 가 나오기 전까지 계속 데크에 저장
    
    elif (i=='>'):
        queue.append(i)
        for i in range(len(queue)):
            result.join(queue.popleft()) # 앞에서 부터 출력

    elif (i==' '):
        for i in range(len(queue)):
            result.join(queue.pop()) # 뒤에서 부터 출력
    else:
        queue.append(i)    

# <>안에 있는 공백 처리 문제