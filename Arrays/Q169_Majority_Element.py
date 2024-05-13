class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Brute Forch approach Time Limit Exceeded
        # 41/51 Test case Passsed
        # n = len(nums)
        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if(nums[j]==nums[i]):
        #             count+=1
        #     if count > n//2:
        #         return nums[i]
        # return 0

        
        # Optimal Approach
        # Moore's Voting Algorithm
        n = len(nums)
        count = 0
        element = None
        for i in range(n):
            if count ==0:
                count =1
                element = nums[i]
            elif element == nums[i]:
                count+=1
            else:
                count-=1
        count_1 =0
        for i in range(n):
            if nums[i] == element:
                count_1+=1
        if count_1 > n//2:
            return element
        return 0


        