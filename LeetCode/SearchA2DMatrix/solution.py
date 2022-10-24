class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if self.binary_search(row, target):
                return True
        return False
        

    def binary_search(self, arr, target):
        start, end = 0, len(arr) - 1
        pos = (start + end) // 2

        while start <= end:
            print(pos)
            if target == arr[pos]:
                return True
            
            elif target < arr[pos]:
                # shift left
                end = pos - 1
            
            else:
                start = pos + 1
            pos = (start + end) // 2
        
        return False