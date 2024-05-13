class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Method-1
        # negative=[]
        # positive=[]
        # n = len(nums)
        # for i in range(n):
        #     if nums[i]<0:
        #         negative.append(nums[i])
        #     else:
        #         positive.append(nums[i])
        # for i in range(len(positive)):
        #     nums[2 * i] = positive[i]
        # for i in range(len(negative)):
        #     nums[2 * i + 1] = negative[i]
  
        # return nums

        #Method-2
        n = len(nums)
        result = [0]*n
        p_Index,n_Index =0,1
        for i in range(n):
            if(nums[i]<0):
                result[n_Index]=nums[i]
                n_Index+=2
            else:
                result[p_Index] = nums[i]
                p_Index+=2
        return result