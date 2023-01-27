'''
233. Number of Digit One

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example 1:
Input: n = 13
Output: 6

Example 2:
Input: n = 0
Output: 0
 
Constraints:
0 <= n <= 10**9
'''
from collections import Counter
class Solution:
    def get_sub_count(self, n, current_count):
        if n == 0: return 0
        if n >= 1 and n < 10: return 1
        scale = len(str(n))-1
        if scale >= 1:
            current_count += (10**(scale-1) * scale) + 1
        n -= 10**scale
        current_count += self.get_sub_count(n, current_count)
        return current_count

    def countDigitOne(self, n: int) -> int:
        return self.get_sub_count(n, 0)
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.countDigitOne(1))
    print(solution.countDigitOne(10))
    print(solution.countDigitOne(13))
    print(solution.countDigitOne(100))
    print(solution.countDigitOne(200))
    print(solution.countDigitOne(300))
    print(solution.countDigitOne(1000))
    print(solution.countDigitOne(10000))
    print(solution.countDigitOne(100000))
    print(solution.countDigitOne(1000000))
    print(solution.countDigitOne(10000000))
    print(solution.countDigitOne(100000000))
    print(solution.countDigitOne(1000000000))
