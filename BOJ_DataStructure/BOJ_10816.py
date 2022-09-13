import sys

result = {}
n = int(sys.stdin.readline())

intCard = sys.stdin.readline().split() # type: str

m = int(sys.stdin.readline())
question = sys.stdin.readline().split() # type: str
for num in question:
    result[num] = 0

for num in intCard:
    try:
        result[num] += 1
    except KeyError:
        pass

print(' '.join(map(str, result.values())))