from cgitb import reset
import sys

# n = int(sys.stdin.readline())

# result = []
# for i in range(n):
#     num = int(sys.stdin.readline())

#     result.append(num)

# result.sort()

# for i in range(n):
#     result[i] = str(result[i])

# print('\n'.join(result))

# ------------------------

n = int(sys.stdin.readline())

result = []

for i in range(n):
    num = int(sys.stdin.readline())

    result.append(num)

    for j in range(len(result)):
        if len(result) == 1:
            pass
        else:
            if result[j-1] > result[j]:
                result[j-1], result[j] = result[j], result[j-1]
            else:
                min = result[j]

for i in range(n):
    result[i] = str(result[i])

print('\n'.join(result))