from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())   
position = list(map(int, input().split()))  
dq = deque([i for i in range(1, n+1)]) 

count = 0
for i in position: 
    while True:     
        if dq[0] == i:  
            dq.popleft()
            break
        else:
            if 
            
            else:  
                
                
print(count)