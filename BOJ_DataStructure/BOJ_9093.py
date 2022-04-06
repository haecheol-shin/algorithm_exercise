import sys

n = int(sys.stdin.readline()) # 테스트 케이스 개수 입력

wordList = [] # 단어를 저장할 리스트

for i in range(n): # 테스트 케이스 개수만큼 반복
    sentence = sys.stdin.readline() # 문장 입력
    wordList.append(list(sentence.split())) # 공백으로 단어를 구분하고 단어 단위로 리스트에 저장 2차원 배열 생성

    for j in range(len(wordList[i])): # 각 단어의 길이만큼 반복
        wordList[i][j] = wordList[i][j][::-1] # 단어를 뒤집어서 저장

for i in range(n):
    result = '' # 문장을 저장할 빈 문자열, 한번 반복문이 돌면 빈 문자열로 다시 초기화한다
    for j in range(len(wordList[i])):
        result += wordList[i][j] + ' '
    print(result)