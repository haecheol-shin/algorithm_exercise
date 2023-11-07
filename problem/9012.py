import sys

times = int(sys.stdin.readline())

for _ in range(times):
    stack = []
    ps = sys.stdin.readline()
    flag = True

    for i in ps.strip():
        if i == '(':
            stack.append(i)

        else:
            if stack:
                stack.pop()

            else:
                flag = False
                break

    if flag:
        if stack:
            print("NO")
        else:
            print("YES")

    else:
        print("NO")


