class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stonk = 0 
        l, r = 0, 1
        #since its sliding window r should be next to l until greater l appears

        while r != len(prices): 
            stonk = max(stonk, prices[r]-prices[l])
            if prices[l] > prices[r]:
                l += 1
            else:
                r += 1
        return stonk
