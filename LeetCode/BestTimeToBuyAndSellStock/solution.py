class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 1: return 0

        # tracks max profit
        # initialise to 0 (prices are >= 0)
        max_profit = 0
        # sentinel
        min_so_far = 99999

        for i in range(len(prices) - 1):
            # get min_so_far updated
            if min_so_far > prices[i]:
                min_so_far = prices[i]
            
            profit = prices[i+1] - min_so_far
            if profit > max_profit:
                max_profit = profit
        
        return max_profit


