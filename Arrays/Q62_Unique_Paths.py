class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        N = n + m - 2
        r = m - 1
        res = 1
        for i in range(1, r + 1):
            res = res * (N - r + i) / i
        return int(res)