from typing import List


class Solution:
    def two_sum(self, target: int, nums: List[int]) -> List[int]:
        # assumptions: all elements are positive
        for num_a in nums:
            num_b = target - num_a
            if num_b in nums:
                return [nums.index(num_a), nums.index(num_b)]
        # in case no matching pairs available
        print(f'>>> No matching pairs found for target: {target}')


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.two_sum(target, nums))
