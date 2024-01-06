from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for x in prices[1:]:
            if x < min_price:
                min_price = x
                continue
            profit = x - min_price
            if profit > max_profit:
                max_profit = profit
            
        return max_profit

def main(prices):
    print(f'Input: prices = {prices}')
    ret = Solution().maxProfit(prices)
    print(f'Output: {ret}')




if __name__ == "__main__":
    #prices = [7,1,5,3,6,4]
    #prices = [7,6,4,3,1]
    prices = [4]
  
    main(prices)
