class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maximum = 0
        for i in range(len(nums)): #[1,1,0,1,1,1]
            if(nums[i]==1):
                count+=1
            else:
                count = 0
            maximum = max(maximum,count)
        return maximum