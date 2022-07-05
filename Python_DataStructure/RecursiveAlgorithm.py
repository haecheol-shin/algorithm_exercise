# 재귀 알고리즘 중 가장 대표적인 예가 피보나치 순열

def solution(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return solution(x-1) + solution(x-2)

if __name__=="__main__":
    x = int(input())
    print(solution(x))