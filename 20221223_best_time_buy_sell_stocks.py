'''
DAILY PROBLEM - 12-23-2022

309. Best Time to Buy and Sell Stock with Cooldown

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''
class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1: return 0
        prices_length = len(prices)
        i = 1
        profit = 0
        buy = True
        sell = False
        while i < prices_length-1:
            if prices[i+1] < prices[i]:
                if buy:
                    sell = True
                    buy = False
                profit += prices[i] - prices[i-1]
            else:
                if not buy:
                    buy = True
                    sell = False
            i += 1
        return profit

solution = Solution()
print(solution.maxProfit([1,2,3,0,2])) # Expected: 3
print(solution.maxProfit([1])) # Expected: 0
