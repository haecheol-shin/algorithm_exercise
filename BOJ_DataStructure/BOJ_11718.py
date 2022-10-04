import sys

while(l:=sys.stdin.readline()) :
    print(l, end="")

###############################

while(1) :
    try :
        print(input())
    except EOFError:
        break

# sys.stdin.readline() 은 더 이상 읽을게 없으면 빈 문자열을 반환
# 그래서 EOF를 일으키지 않는다.
# input()은 EOF를 일으킨다