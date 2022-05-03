# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys 
n = int(sys.stdin.readline())
deque = []

for i in range(n):
    userCommand = sys.stdin.readline().split()

    if (userCommand[0]=="push_front"):
        deque.insert(0, userCommand[1])

    elif (userCommand[0]=="push_back"):
        deque.append(userCommand[1])
    
    elif (userCommand[0]=="pop_front"):
        if (len(deque)!=0):
            print(deque.pop(0))
        else:
            print(-1) 
    
    elif (userCommand[0]=="pop_back"):
        if (len(deque)!=0):
            print(deque.pop())
        else:
            print(-1) 
    
    elif (userCommand[0]=="empty"):
        if (len(deque)!=0):
            print(0)
        else:
            print(1)

    elif (userCommand[0]=="size"):
        print(len(deque))
    
    elif(userCommand[0]=="front"):
        if (len(deque)!=0):
            print(deque[0])
        else:
            print(-1)

    elif(userCommand[0]=="back"):
        if (len(deque)!=0):
            print(deque[-1])
        else:
            print(-1)
        
    else:
        break
