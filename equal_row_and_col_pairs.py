"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 """
import numpy as np
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid_np = np.array(grid)
        num_pairs = 0
        length = grid_np.shape[0]
        for row in range(length):
            for column in range(length):
                if np.array_equal(grid_np[row,:], grid_np[:,column]):
                    num_pairs += 1
        return num_pairs