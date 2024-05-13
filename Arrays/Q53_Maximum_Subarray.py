class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = nums[0]
        current_sum = 0
        n = len(nums)
        
        for i in range(n):
            current_sum = max(nums[i], current_sum + nums[i])
            maximum = max(maximum, current_sum)
        
        return maximum  
        