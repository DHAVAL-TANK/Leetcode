from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = prices[0]
        maxProf = 0


        for i in range (1,len(prices)):
            if prices[i] > minPrice: 
                maxProf = max (maxProf,prices[i] - minPrice )
            minPrice =  min (prices[i],minPrice)
        return maxProf
        
