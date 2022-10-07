import sys

nums = sys.stdin.readline()
num = []
for i in nums:
    num.append(i)

num.sort(reverse=True)
result = ''
print(result.join(num).rstrip())