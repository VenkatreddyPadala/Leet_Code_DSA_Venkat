class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0 
        right = left+1
        while len(nums)>right:
            if nums[left]==nums[right]:
                del nums[right]
            else:
                left = left+1
                right = left+1
        return len(nums)