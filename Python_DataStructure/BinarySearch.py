# 이진탐색 알고리즘

def solution(L, x):
    lower = 0 # 리스트 맨 앞
    upper = len(L)-1 # 리스트 맨 끝
    while lower<=upper:
        middle = int((lower + upper) / 2) # 소수점 버림
        if L[middle] == x: # data found
            return middle
        elif L[middle] > x: # data < middle value
            upper = middle-1
        else: # data > middle value
            lower = middle+1        
    
    return -1 # data not found

if __name__=="__main__":
    L = [2, 3, 5, 6, 9, 11, 15]
    x = 6
    print(solution(L, x))

    x = 100
    print(solution(L, x))