class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # My logic
        # red = []
        # white = []
        # blue = []
        # n = len(nums)
        
        # for i in range(n):
        #     if nums[i] == 0:
        #         red.append(nums[i])
        #     elif nums[i] == 1:
        #         white.append(nums[i])
        #     else:
        #         blue.append(nums[i])
        
        # r = len(red)
        # w = len(white)
        # b = len(blue)
        
        # for i in range(r):
        #     nums[i] = red[i]
        # for i in range(r, r + w):
        #     nums[i] = white[i - r]
        # for i in range(r + w, n):
        #     nums[i] = blue[i - r - w]
        
        # return nums
        
        # optimal Approach
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        