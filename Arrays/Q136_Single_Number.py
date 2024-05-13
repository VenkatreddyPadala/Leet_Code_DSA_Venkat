class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # for i in range(n):
        #     number = nums[i]
        #     count=0
        #     for j in range(n):
        #         if nums[j]==number:
        #             count = count+1
        #     if count==1:
        #         return number
        # return 0

        #Optimized One
        result = 0
        for num in nums:
            result ^= num
        return result