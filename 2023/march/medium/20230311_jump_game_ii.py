'''
45. Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], 
you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 10**4
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
'''

class Solution:
    def jump(self, nums) -> int:
        if len(nums) == 1: return 0
        if len(nums) == 2: return 1
        if nums[0] >= len(nums)-1: return 1
        if len(list(set(nums[:-1]))) == 1: return len(nums)-nums[0]

        i = 0
        min_jump = 0
        while True:
            x+=1
            if nums[i] >= len(nums[i+1:]):
                min_jump += 1
                nums = nums[:i+1]
                if len(nums[:i+1]) <= 1:
                    return min_jump
                i = 0
            else:
                i += 1
    
print(Solution().jump([2,3,1,1,4])) # 2
print(Solution().jump([2,3,0,1,4])) # 2
print(Solution().jump([1,1,1,1])) # 3
print(Solution().jump([2,2,2,2])) # 2