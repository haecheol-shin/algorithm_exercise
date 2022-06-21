# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

result = 0
snakeLength = 1 # 처음위치 좌측맨위, 처음에 오른쪽을 향함

size = int(input()) # 보드의 크기
board = [ [] for _ in range(size) ]
for i in range(size):
    board[i] = [0 for _ in range(size) ]
        
numApple = int(input()) # 사과 개수
for i in range(numApple):
    locationApple = list(map(int, input().split()))
    board[locationApple[0]][locationApple[1]] = 1 # 사과 위치 정보 저장

numDirect = int(input()) # 방향 정보 개수
for i in range(numDirect):
    locationSnake = list(input().split())
    snakeHead = 0 # 1초마다 1씩 증가
    snakeTail = 0

    for j in range(locationSnake[0]):
        stack = []
        stack.append()
    # 뱀이 움직이는 경로를 그려야한다. 데크 or 스택으로 처리할듯


    if (snakeHead > size):
        break
    
    # 뱀의 머리가 보드 벽에 부딪히면 break

    result = result + locationSnake[0]
