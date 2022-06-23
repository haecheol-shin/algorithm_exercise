import sys
import heapq

n = int(sys.stdin.readline())
heap = [] # 힙

for i in range(n):
    num = int(sys.stdin.readline())
    if num!=0: # 0이 아닐때만 저장
        heapq.heappush(heap, num)

    if num==0 and len(heap)==0: # 힙의 크기가 0이면 0 출력
        print(0)
    
    elif num==0 and len(heap)!=0:
        print(heapq.heappop(heap))

# n번반복에다가 sort가 들어가서 시간초과 뜨는 듯
# heapq 모듈이 있는데 그걸 써야 하는 듯
# 이진트리기반 최소 힙을 생성함.
# 내부적으로 트리구조를 만듬
# 그냥 리스트는 O(n)이면 최소힙은 O(logn)

# 그냥 최솟값을 얻고 싶다면 pop하지 않고 0번째 인덱스에 접근하면 된다.