"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int])-> int:
        current_max = []
        left_index, right_index = 0, len(height)-1
        while left_index < len(height):
            if left_index == right_index:
                return max(current_max)
            width, length = right_index - left_index, min(height[left_index], height[right_index])
            area = length * width
            current_max.append(area)
            if height[left_index] < height[right_index]:
                left_index += 1
            else:
                right_index -= 1
        return max(current_max)

if __name__ == "__main__":
    sol = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(height))