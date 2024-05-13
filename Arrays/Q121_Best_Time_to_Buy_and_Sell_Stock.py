class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Lets consider this as BruteForce Approch 
        # Time Limit Exceeded Error 198/212 Test Cases
        # maxi = 0
        # n = len(prices)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if(prices[j]>prices[i]):
        #             maxi = max(prices[j]-prices[i],maxi)
        # return maxi

        # Optimal 
        # maximum_profit = 0
        # minimum_price = prices[0]
        # n = len(prices)
        # for i in range(1,n): 
        #     minimum_price = min(minimum_price,prices[i])
        #     maximum_profit = max(maximum_profit,prices[i]-minimum_price)
        # return maximum_profit

        #optimal-2
        if len(prices)==0:
            return 0
        mi=prices[0]
        r=0
        for i in prices:
            diff= i-mi
            if diff>r:
                r=diff
            if i<mi:
                mi=i
        return r