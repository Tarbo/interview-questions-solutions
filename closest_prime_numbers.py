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
        is_prime = [True] * (right + 1)
        p = 2
        while p * p <= right:
            if is_prime[p]:
                for i in range(p * p, right + 1, p):
                    is_prime[i] = False
            p += 1
        
        # Collect all prime numbers in the range [left, right]
        prime_nums = [num for num in range(max(2, left), right + 1) if is_prime[num]]
        
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
    left, right = 1, 1000000
    sol = Solution()
    print(sol.closestPrimes(left, right))


