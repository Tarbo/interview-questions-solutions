"""
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0"""
from typing import List


class Solution:
    def are_opposite_signs(self, a:int, b:int)-> bool:
        return (a > 0 and b < 0) or (a < 0 and b > 0)
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stable_stack = []
        for asteroid in asteroids:
            if len(stable_stack) == 0 or self.are_opposite_signs(asteroid, stable_stack[-1]) == False:
                stable_stack.append(asteroid)
            while len(stable_stack) != 0 and self.are_opposite_signs(asteroid, stable_stack[-1]):
                if abs(asteroid) > abs(stable_stack[-1]):
                    # top of the stack explodes
                    stable_stack.pop() 
                elif abs(asteroid) < abs(stable_stack[-1]):
                    # current asteroid explodes
                    break
                else:
                    stable_stack.pop()
                    break
        return stable_stack
    
if __name__ == "__main__":
    asteroids = [-2,-1,1,2]
    sol = Solution()
    print(sol.asteroidCollision(asteroids))
                 
