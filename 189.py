class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        moveFactor = k%len(nums)
        ret = nums[len(nums)-moveFactor:] + nums[:len(nums)-moveFactor]
        for i in range(len(nums)):
            nums[i] = ret[i]

            
#tried making it shorter but the object pointer wouldnt change
# moveFactor = k%len(nums)
# nums = nums[len(nums)-moveFactor:] + nums[:len(nums)-moveFactor]
#if I could return this object instead, then this solution should work