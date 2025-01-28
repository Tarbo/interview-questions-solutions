"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)"""
import copy
import math
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Since O(n) is required, I will try the bruteforce approach.
        nums2 = nums.copy()
        for index in range(len(nums)):
            if index == 0:
                nums2[index] = math.prod(nums[1:])
            elif index == len(nums2)-1:
                nums2[index] = math.prod(nums[:-1])
            else:
                new_list = nums[:index] + nums[index+1:]
                print(f"Index {index}:\t{new_list}")
                nums2[index] = math.prod(new_list)

        return nums2

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4]
    print(solution.productExceptSelf(nums=nums))

