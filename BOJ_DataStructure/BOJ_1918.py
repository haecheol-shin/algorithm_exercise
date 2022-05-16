sentence = input()
stack = []
dic = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}
result = ''

for i in range(len(sentence)):
    if (sentence[i].isalpha()==True):
        result = result + sentence[i]
    
    else:
        if sentence[i]=='(' or sentence[i]==')':    
            if sentence[i]=='(':
                stack.append(sentence[i])
                pass

            if sentence[i]==')':
                for j in range(len(stack)):
                    result = result + stack.pop()
                    if (sentence[j]=='('):
                        break

        else:                
            if len(stack)==0 or dic[stack[-1]]<dic[sentence[i]]:
                    stack.append(sentence[i])
                    pass

            else:
                for k in range(len(stack)):
                    # should print AB*CD*E/-, but prints AB*CD*-E/ sentence[k]
                    if len(stack)>=2 and dic[stack[-1]]==dic[sentence[i]] and dic[stack[-1]]<dic[stack[-2]]:
                        break
                    else:
                        if dic[stack[-1]]<dic[sentence[i]]:
                            break
                        result = result+stack.pop()
                stack.append(sentence[i])

for i in range(len(stack)):
    result = result+stack.pop()
print(result.replace('(', ''))
