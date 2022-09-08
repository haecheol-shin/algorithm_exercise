import sys

def star(l):
    if l == 3:
        return ['***','* *','***']

    arr = star(l//3)
    stars = []

    for i in arr:
        stars.append(i*3)

    for i in arr:
        stars.append(i+' '*(l//3)+i)

    for i in arr:
        stars.append(i*3)

    return stars

n = int(sys.stdin.readline())
print('\n'.join(star(n))) # 리스트에 join을 하면 요소 하나당 그 문자를 붙여서 출력해준다.
