"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_count = {num:0 for num in nums}
        for num in nums:
            dict_count[num] = 1
        return [num for num in dict_count.keys() if dict_count[num] == 1][0]

if __name__ == "__main__":
    nums = [4,1,2,1,2]
    sol = Solution()
    print(sol.singleNumber(nums))