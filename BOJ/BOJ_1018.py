n,m = map(int, input().split()) # n이 세로줄 수, m이 가로줄 수

chess_board = []

for i in range(n):
    for j in range(m):
        chess_board[i][j] = input()
        
for i in range(n):
    for i in range(m):
        print(chess_board[n][m])
    print()