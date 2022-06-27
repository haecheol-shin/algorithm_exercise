import sys
import heapq

n = int(sys.stdin.readline())
maxHeap = [] # 최대 힙

for i in range(n):
    num = int(sys.stdin.readline())
    if num!=0: # 0이 아닐때만 저장
        heapq.heappush(maxHeap, (-num, num)) # 최대 힙으로 사용하기 위해 튜플 형태로 원소 삽입

    if num==0 and len(maxHeap)==0: # 힙의 크기가 0이면 0 출력
        print(0)
    
    elif num==0 and len(maxHeap)!=0:
        print(heapq.heappop(maxHeap)[1]) # 튜플 형태로 저장된 원소의 첫번째 인덱스 값을 사용한다.
        