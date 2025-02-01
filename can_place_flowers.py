"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num_vacant_plots = 0
        l = len(flowerbed)
        for i in range(len(flowerbed)):
            check = False
            if l == 1:
                num_vacant_plots = 1 - flowerbed[0]
            if i == 0 and l > 1:
                check = (flowerbed[i] == flowerbed[i+1] == 0)
                num_vacant_plots += 1 if check else 0
            elif i == l - 1 and l > 1:
                check = (flowerbed[-1] == flowerbed[-2] == 0)
                num_vacant_plots += 1 if check else 0
            elif i != 0 and i != l-1 and l > 1:
                check = (flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0)
                num_vacant_plots += 1 if check else 0
            if check:
                flowerbed[i] = 1
        return n <= num_vacant_plots


if __name__ == "__main__":
    sol = Solution()
    flowerbed = [0]
    n = 1
    print(sol.canPlaceFlowers(flowerbed, n))