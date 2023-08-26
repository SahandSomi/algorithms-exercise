import pytest

class Solution(object):

    def best_time_to_buy_and_sell_stock_SS(self, prices):

        best_price = 0
        min_value = prices[0]

        for i in range(1,len(prices)):

            if prices[i]<min_value:
                min_value = prices[i]
            best_price = max(best_price, (prices[i]-min_value))

        return best_price
    
    def best_time_to_buy_and_sell_stock_neat(self, prices):
        
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res
            
# Guide for solution:
# Brute Force: check every combinations O(n2)
# window O(n)
### Golden rule: 