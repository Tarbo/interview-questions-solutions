"""You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_costs = [0] * len(cost)
        min_costs[-2] = cost[-2]
        if len(cost) > 2:
            for i in range(len(cost)-3, 0,-1):
                print(f'i = {i}')
                min_costs[i] = cost[i] + min(min_costs[i+1], min_costs[i+2])
            min_costs[0] = cost[0] + min(min_costs[1], min_costs[2])
        print(min_costs)
        return min(min_costs[0], min_costs[1])
if __name__ == "__main__":
    cost = [1,100,1,1,1,100,1,1,100,1]
    sol = Solution()
    print(sol.minCostClimbingStairs(cost))
