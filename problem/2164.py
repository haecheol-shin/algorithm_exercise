import sys
from collections import deque

n = int(sys.stdin.readline())

cards = deque()
for i in range(1, n+1):
    cards.append(i)

count = 0
while len(cards) != 1:
    count += 1
    if count % 2 == 1:
        cards.popleft()

    else:
        cards.append(cards.popleft())

print(cards.pop())

# --------------------------------

import sys
from collections import deque

n = int(sys.stdin.readline())

cards = deque(range(1, n+1))

while len(cards) != 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards.pop())