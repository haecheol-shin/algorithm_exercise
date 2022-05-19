import sys

def letterCount(sentence):
    upperCount = 0
    lowerCount = 0
    numCount = 0
    spaceCount = 0

    for letter in sentence:
        if letter.islower():
            lowerCount += 1
        
        elif letter.isupper():
            upperCount += 1
        
        elif letter.isdigit():
            numCount += 1
        
        elif letter.isspace():
            spaceCount += 1
        
        else:
            return -1
    
    result = str(lowerCount)+' '+str(upperCount)+' '+str(numCount)+' '+str(spaceCount)
    return result

if __name__=="__main__":
        while True: #  EOF 종료조건 기억
            try:
                sentence = input()
                func = letterCount(sentence)
                if func == -1:
                    break
                    
                else:
                    print(func)

            except EOFError:
                break
        # n = int(input())
            
        # sentenceList = []

        # for i in range(n):
        #     sentenceList.append(sys.stdin.readline())
        
        # for i in sentenceList:
        #     letterCount(i)