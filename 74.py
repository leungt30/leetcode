class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        low = 0
        high = len(matrix)*n-1
        while (low <= high):
            mid = (low+high)//2
            current = matrix[mid//n][mid%n]
            if (target > current):
                low = mid+1
            elif (target < current):
                high=mid-1
            else:
                return True
        return False