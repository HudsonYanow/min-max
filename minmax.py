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
        self.arr = arr

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
        """
        Finds the `n` smallest values in the list.

        Args:
            n (int): The number of smallest values to find.

        Returns:
            list: A list of the `n` smallest numbers in ascending order.
        """
        smallNum = []
        carr = self.arr.copy()
        for _ in range(n):
            min_val = carr[0]
            for num in carr:
                if num < min_val:
                    min_val = num
            smallNum.append(min_val)
            carr.remove(min_val)
        return smallNum

    def getMax(self):
        """
        Finds the largest value in the list.

        Returns:
            int/float: The largest number in the list.
        """
        max_val = self.arr[0]
        for num in self.arr:
            if num > max_val:
                max_val =
