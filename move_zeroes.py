"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Optimal solution: Solve the optimal way the next time.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_non_zero = [num for num in nums if num != 0]
        length_nums = len(nums)
        num_zeros = length_nums - len(nums_non_zero)
        zeros_pad = [0]*num_zeros
        nums.extend(nums_non_zero)
        nums.extend(zeros_pad)
        nums[:] = nums[length_nums:]

if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,0,3,12]
    sol.moveZeroes(nums)
    print(nums)