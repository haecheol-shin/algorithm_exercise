def solution(L, x, l, u): # L은 리스트, x는 찾고자 하는 원소, l은 lower, u는 upper
    if l>u: # =이 들어가면 안된다. 찾고자 하는 원소가 없을 때
        return -1
    mid = (l + u) // 2
    if x == L[mid]: # data found
        return mid
    elif x < L[mid]: # data < middle value
        return solution(L, x, l, mid-1)

    else: # data > middle value
        return solution(L, x, mid+1, u)

if __name__=="__main__":
    L = [3, 8, 2, 7, 6, 5, 10, 1]
    print(solution(L, 4, 0, len(L)-1))
    print()
    print(solution(L, 10, 0, len(L)-1))

# 재귀 알고리즘이 구현에는 더 유리할 수 있으나 시간적인 효율 측면에서는 반복구조가 더 나을 수 있다.