"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        max_operations = 0
        nums.sort()
        left_index, right_index = 0, len(nums)-1
        while left_index < right_index:
            k_sum = nums[left_index]+nums[right_index]
            if k == k_sum:
                max_operations += 1
                left_index += 1
                right_index -= 1
            elif k > k_sum:
                left_index += 1
            else:
                right_index -= 1
        return max_operations
    
if __name__ == "__main__":
    sol = Solution()
    nums = [2,2,2,3,1,1,4,1]
    k = 4
    print(sol.maxOperations(nums, k))


