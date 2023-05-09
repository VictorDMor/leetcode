'''
220. Contains Duplicate III

You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:
i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and

Return true if such pair exists or false otherwise.

Example 1:
Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

Example 2:
Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.

Constraints:

2 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9
1 <= indexDiff <= nums.length
0 <= valueDiff <= 10**9
'''

from typing import List
from sortedcontainers import SortedList # External library, use pip to install it

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = SortedList()
        for i in range(len(nums)):
            if i > indexDiff:
                window.remove(nums[i-indexDiff-1])
            j = window.bisect_left(nums[i]-valueDiff)
            if j < len(window) and abs(nums[i]-window[j]) <= valueDiff:
                return True
            if j > 0 and abs(nums[i]-window[j-1]) <= valueDiff:
                return True
            window.add(nums[i])
        return False

