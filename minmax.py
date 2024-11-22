import BL

class MinMax:
    """
    A class to find the minimum and maximum values, as well as ranges of these values, 
    in a given list of numbers.

    Attributes:
        arr (list): The list of numbers to process.
    """

    def __init__(self, arr):
        """
        Initializes the MinMax object with a list of numbers.

        Args:
            arr (list): A list of numeric values.
        """
        if BL.listTypeValidator(arr, int):
            self.arr = arr
        else:
            print("the list contains a item that is not a number")

    def getMin(self):
        """
        Finds the smallest value in the list.

        Returns:
            int/float: The smallest number in the list.
        """
        min_val = self.arr[0]
        for num in self.arr:
            if num < min_val:
                min_val = num
        return min_val

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
