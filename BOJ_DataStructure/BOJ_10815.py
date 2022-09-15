import sys

n = int(sys.stdin.readline().rstrip())
intCard = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
question = list(map(int, sys.stdin.readline().rstrip().split()))

result = {}
for num in intCard:
    if num not in result:
        result.setdefault(num, 1)
    
    else:
        result.update({num:result.get(num)+1})

for num in question:
    if result.get(num) == None:
        print(0, end=' ')
    
    else:
        print(1, end=' ')