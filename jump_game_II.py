"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

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

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1]."""
class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_min_sum = [10000] * len(nums)
        nums_len = len(nums)
        if nums_len == 1:
            return 0
        # find the min jumps in reverse order at each point
        for index in range(nums_len - 2, -1, -1):
            if nums[index] != 0:
                if nums[index] >= nums_len-index-1:
                    jump_min_sum[index] = 1
                else:
                    jump_min_sum[index] = 1 + min(jump_min_sum[index+1:index+1+nums[index]])
        return jump_min_sum[0]
    
if __name__ == "__main__":
    nums = [2,3,0,1,4]
    sol = Solution()
    print(sol.jump(nums))
        