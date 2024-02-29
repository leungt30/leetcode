class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # base case
        arr = [[1]]

        for i in range(1,numRows):
            # current array, filled with 1's so both ends are 1
            carr = [1 for _ in range(i+1)] #length i+1 based on pascal triange length per level
            # fill in every box except the first and last
            for j in range(1,i):
                # pascal triange defintion
                carr[j] = arr[i-1][j-1] + arr[i-1][j]
            # add to the answer
            arr.append(carr)
        return arr


