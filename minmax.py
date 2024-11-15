class MinMax:
    def __init__(self, arr):
        self.arr=arr
    def getMin(self):
        min=self.arr[0]
        for num in self.arr:
            if num<min:
                min=num
        return min
    def getMinRange(self, n):
        smallNum=[]
        carr=self.arr.copy()
        for i in range(n):
            min=carr[0]
            for num in carr:
                if num<min:
                    min=num
            smallNum.append(min)
            carr.remove(min)
        return smallNum
    def getMax(self):
            max=self.arr[0]
            for num in self.arr:
                if num>max:
                    max=num
            return max
    def getMaxRange(self, n):
        bigNum=[]
        carr=self.arr.copy()
        for i in range(n):
            max=carr[0]
            for num in carr:
                if num>max:
                    max=num
            bigNum.append(max)
            carr.remove(max)
        return bigNum      
min=MinMax([3,7,20,15,2])
print(min.getMin())
print(min.getMinRange(3)) 
print(min.getMax())
print(min.getMaxRange(3))