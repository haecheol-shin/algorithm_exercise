# 사용자에게 문장을 한꺼번에 받는지 or 한문장씩 받는지

upperCaseLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upperDic = {}

lowerCaseLetter = "abcdefghijklmnopqrstuvwxyz"
lowerDic = {}

numberLetter = '0123456789'
numDic = {}

space = 0 # 공백
num = 0 # 숫자
upper = 0 # 대문자
lower = 0 # 소문자

sentence = input().split('\n')
print(sentence)
# for letter in sentence:
