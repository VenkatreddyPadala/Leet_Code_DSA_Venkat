class Solution(object):
    def check(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        k = sorted(nums)
        for i in range(n):
            rotated = nums[i:] + nums[:i]
            if rotated == k:
                return True
        
        return False

if __name__ == '__main__':
    nums = eval(input("Enter the Array"))
    s = Solution.check(nums)
    print(s)