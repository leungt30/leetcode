class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [1]
        for i in range(1,rowIndex+1):
            carr = [1 for _ in range(i+1)]
            for j in range(1,i):
                carr[j] = arr[j-1] + arr[j]
            arr = carr
        return arr