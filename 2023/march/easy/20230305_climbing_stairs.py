'''
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
'''
# By looking at the outputs and creating more testcases I learned that this is a classic Fibonacci sequence. 
# Since for large values we were reaching timeout exception, I decided to implement some caching to not overload the recursion depth
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def fib_sequence(n, cache):
            if n in cache:
                return cache[n]

            if n <= 2:
                return 1
            else:
                cache[n] = fib_sequence(n-2, cache) + fib_sequence(n-1, cache)
                return cache[n]
        
        return fib_sequence(n+1, cache)