'''
41. First Missing Positive

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 
Constraints:
1 <= nums.length <= 10**5
-2**31 <= nums[i] <= 2**31 - 1
'''

class Solution:
    def firstMissingPositive(self, nums):
        if 1 not in nums:
            return 1
        else:
            positives_sorted = sorted([n for n in nums if n > 0])
            for i in range(1, len(positives_sorted)):
                if positives_sorted[i] - positives_sorted[i-1] > 1:
                    return positives_sorted[i-1] + 1
        return max(nums)+1


print(Solution().firstMissingPositive([1,2,0]))
print(Solution().firstMissingPositive([3,4,-1,1])) # -1, 1, 3, 4
print(Solution().firstMissingPositive([7,8,9,11,12]))
print(Solution().firstMissingPositive([0]))
print(Solution().firstMissingPositive([2147483647]))
