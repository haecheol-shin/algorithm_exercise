# upperLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# lowerLetter = "abcdefghijklmnopqrstuvwxyz"

# upperDic = {}
# lowerDic = {}

# i = 0
# for spelling in upperLetter:
#     upperDic[spelling] = i
#     i = i+1

# j = 0
# for spelling in lowerLetter:
#     lowerDic[spelling] = j
#     j = j+1

# sentence = input()
# result = ''

# for letter in sentence:
#     if letter.isupper():
#         upperIndex = upperDic[letter] + 13
#         if upperIndex > 25:
#             upperIndex = upperIndex - 25
#         result = result + str(upperDic.get(upperIndex))

#     elif letter.islower():
#         lowerIndex = lowerDic[letter] + 13
#         if lowerIndex > 25:
#             lowerIndex = lowerIndex - 25
#         result = result + str(lowerDic.get(lowerIndex))
    
#     else:
#         result = result + letter

# print(result)

sentence = input()
result = ''

for letter in sentence:
    if letter.isupper():
        rot13 = ord(letter)+13
        if rot13 > 90:
            rot13 = rot13 - 26
        result = result + chr(rot13)

    elif letter.islower():
        rot13 = ord(letter)+13
        if rot13 > 122:
            rot13 = rot13 - 26
        result = result + chr(rot13)
    
    else:
        result = result + letter

print(result)