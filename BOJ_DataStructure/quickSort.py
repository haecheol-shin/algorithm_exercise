def q_s(start, last):
    print("정렬")
    i = start
    j = last
    data = a[start]

    if (start<last):
        while(i<j):
            while(a[i]<=data):
                i = i+1
            while(a[j]>data):
                j = j-1
            
            if(i<j):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
        
        temp = a[start]
        a[start] = a[j]
        a[j] = temp

        for k in range(len(a)):
            print(a[k], end=' ')
        print()
        q_s(start, j-1)
        q_s(j+1, last)


if __name__=="__main__":
    a = [14, 5, 43, 27, 18, 31, 37, 88, 6, 35]
    print("<원래배열>")
    for i in range(len(a)):
        print(a[i], end=' ')
    print()
    q_s(0,9)

