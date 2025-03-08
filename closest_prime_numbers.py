"""
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 

Constraints:

1 <= left <= right <= 106"""
class Solution:      
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # generate prime numbers
        nums = range(left,right+1)
        max_num_mar = int(right ** 0.5)
        nums_bool = [True] * len(nums)
        # mark the composites and remove
        for index in range(len(nums)):
            for num in range(2, max_num_mar+1):
                if nums[index] % num == 0:
                    nums_bool[index] = False
                    break
        prime_nums = [nums[i] for i in range(len(nums)) if nums_bool[i] and nums[i] > 1]
        if len(prime_nums) < 2:
            return [-1, -1]
        min_dist = float('inf')
        righ_num = 0
        left_num = 0
        for index in range(len(prime_nums)-1, 0, -1):
            if prime_nums[index] - prime_nums[index-1] <= min_dist:
                min_dist = prime_nums[index] - prime_nums[index-1]
                righ_num = prime_nums[index]
                left_num = prime_nums[index-1]
        return [left_num, righ_num]

    
if __name__ == "__main__":
    left, right = 1, 2
    sol = Solution()
    print(sol.closestPrimes(left, right))


