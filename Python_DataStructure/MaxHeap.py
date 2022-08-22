class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        if self.data == [None]:
            pass
            
        else:
            parentIndex = self.data.index(item)//2
            itemIndex = self.data.index(item)

            while(self.data[parentIndex]<self.data[itemIndex]):
                parentIndex, itemIndex = itemIndex, parentIndex
                parentIndex = parentIndex // 2
                
            
        
def solution(x):
    return 0