class Solution:
    
    def maximumCount(self, nums: List[int]) -> int:
        pcount = 0
        ncount = 0
        for index,item in enumerate(nums):
            if item < 0:
                ncount +=1
            if item > 0:
                pcount = len(nums) - index
                break
        return max(pcount,ncount)