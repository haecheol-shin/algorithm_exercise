expression = list(input())
slice_index = []

for i in range(len(expression)):
    if ('-'==expression[i]):
        slice_index = i

for i in range(len(slice_index)):
    
