import sys

books = {}

for _ in range(int(sys.stdin.readline())):
    book = sys.stdin.readline()

    if book in books:
        books[book] += 1

    else:
        books[book] = 1

bestsellers = []
for k, v in books.items():
    if v == max(books.values()):
        bestsellers.append(k)

bestsellers.sort()
print(bestsellers[0])