class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        n = len(nums)
        k %= n
        j = 0
        while k > 0:
            for _ in range(k):
                nums[j], nums[n - k + j] = nums[n - k + j], nums[j]
                j += 1
            n -= k
            k %= n