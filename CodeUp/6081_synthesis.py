a = int(input(),16)

for i in range(15):
    print('%X'%a, '*%X'%(i+1), '=%X'%(a*(i+1)), sep='')