"""
ou are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_jump = [False] * len(nums)
        nums_length = len(nums)
        for index in range(len(nums)-1,-1,-1):
            if any(can_jump[index+1:min(index+1+nums[index], nums_length-1)]) or nums[index] >= nums_length - index - 1:
                can_jump[index] = True
        return can_jump[0]
    
if __name__ == "__main__":
    nums = [1,2,3]
    sol = Solution()
    print(sol.canJump(nums))