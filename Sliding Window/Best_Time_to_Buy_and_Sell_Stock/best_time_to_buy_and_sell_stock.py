import pytest

class Solution(object):

    def best_time_to_buy_and_sell_stock_SS(self, prices):

        best_price = 0
        min_value = prices[0]

        for i in range(1,len(prices)):

            best_price = max(best_price, (prices[i]-min_value))
            if prices[i]<min_value:
                min_value = prices[i]

        return best_price
    
    def best_time_to_buy_and_sell_stock_neat(self, nums):
        
        pass
            
# Guide for solution:
# Brute Force: check every combinations O(n2)
# window O(n)
### Golden rule: 