def func(sentence):
    stack = []
    for letter in sentence:
        if letter == '(':
            stack.append(letter)
        
        elif letter == '[':
            stack.append(letter)
        
        elif letter == ')':
            if len(stack)==0 or stack[-1] != '(':
                return print('no')
            else:
                stack.pop()
        
        elif letter == ']':
            if len(stack)==0 or stack[-1] != '[':
                return print('no')
            else:
                stack.pop()

        else:
            pass

    if len(stack)!=0:
        return print('no')
    else:
        return print('yes')

if __name__=="__main__":
    while True:
        try:
            sentence = input()
            if sentence == '.':
                break
            
            else:
                func(sentence)
        except EOFError:
            break