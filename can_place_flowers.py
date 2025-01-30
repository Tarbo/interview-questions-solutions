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
        first_plot = flowerbed[0]
        num_vacant_plots = 0
        if len(flowerbed) == 1 & n > 0:
            num_vacant_plots = 1 - first_plot
        elif first_plot == 1 or first_plot == flowerbed[1] == 0:
            plots = flowerbed[::2]
            num_vacant_plots = len(plots) - sum(plots)
        else:
            plots =flowerbed[1::2]
            num_vacant_plots = len(plots) - sum(plots)
        return n <= num_vacant_plots
if __name__ == "__main__":
    sol = Solution()
    flowerbed = [1,0,0,0,0,1]
    n = 2
    print(sol.canPlaceFlowers(flowerbed, n))