class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pointer = 1
        for i in range(len(nums)):
            if (nums[pointer-1] != nums[i]):
                nums[pointer] = nums[i]
                pointer +=1
        return pointer


#OLDER VERSION (newer removes some redundant variables)
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         current = nums[0]
#         pointer = 1
#         for i in range(len(nums)):
#             if (current != nums[i]):
#                 nums[pointer] = nums[i]
#                 current = nums[i]
#                 pointer +=1
#         return pointer