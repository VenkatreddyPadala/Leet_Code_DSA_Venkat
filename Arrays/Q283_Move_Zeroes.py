class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp =[]
        for i in range(len(nums)):
            if nums[i]!=0:
                temp.append(nums[i])
        new_length = len(temp)
        for i in range(new_length):
            nums[i] = temp[i]
        for i in range(new_length,len(nums)):
            nums[i] = 0
        return nums