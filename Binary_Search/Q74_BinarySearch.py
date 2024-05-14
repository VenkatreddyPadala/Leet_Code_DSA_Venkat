class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid = low + (high-low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
        return -1        
    
# Lets Understand this code that 
# to Perfor the binary search first of all array must be sorted 
# lets assume that array is sorted
# our array is nums = [-1,0,3,5,9,12] and target is 9 
# so we have to get the length of the array as it is 6
# initalize low and high as the start and end of the array 0 and n-1 respectively
# while low <= high 
# we are gonna find the mid value 
# if the mid is target you will return it as mid
# if mid is less than the target that mean target is in the  right hand side of the array so we will move the low to mid +1 so that it will be completed in less time
# if mid is greater than the raget that mean the target is in the left hand side of the array so we will move the hight to mid-1 so that it wil be completed in less time
# This is the Explanation of the Problem 
# If the target is not in the array just return -1