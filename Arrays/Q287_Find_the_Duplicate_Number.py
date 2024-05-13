class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # My solution -1
        # left = 0
        # right = left+1
        # nums.sort()
        # while right < len(nums):
        #     if(nums[left]==nums[right]):
        #         return nums[left]
        #     else:
        #         left+=1
        #         right = left+1
        
        # Optimal Solution
        n = len(nums)
        freq = [0] * (n + 1)
        for i in range(n):
            if freq[nums[i]] == 0:
                freq[nums[i]] += 1
            else:
                return nums[i]
        return 0