letters = 'abcdefghijklmnopqrstuvwxyz'
dic = {}

for spelling in letters: # -1로 값 초기화
    dic[spelling] = -1

indexCount = 0
for spelling in input(): # 단어에 있는 스펠링만큼 반복
    if dic[spelling] != -1: # 처음나온 스펠링 위치만 계산
        pass
    else:
        dic[spelling] = indexCount
    
    indexCount += 1


print(' '.join(map(str, dic.values())))