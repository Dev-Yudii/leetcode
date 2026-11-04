"""
This problem was extracted on 2026-10-30 15:32 (UTC-3) from LeetCode at https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/.
You can check the full problem description there.
Problem Title:
    Shortest Path With At Most K Consecutive Identical Characters
Difficulty:
    Medium
Tags:
    String, Graph Theory, Heap (Priority Queue), Shortest Path
"""

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1  |  Expected Output: 3
    inputs1 = {'n': 3, 'edges': [[0, 1, 1], [1, 2, 1], [0, 2, 3]], 'labels': 'aab', 'k': 1}
    print(f'Test 1 Result:', solution.shortestPath(**inputs1), ' | Expected:', 3)

    # Example Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2  |  Expected Output: 2
    inputs2 = {'n': 3, 'edges': [[0, 1, 1], [1, 2, 1], [0, 2, 3]], 'labels': 'aab', 'k': 2}
    print(f'Test 2 Result:', solution.shortestPath(**inputs2), ' | Expected:', 2)

    # Example Input: n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2  |  Expected Output: -1
    inputs3 = {'n': 3, 'edges': [[0, 1, 1], [1, 2, 1]], 'labels': 'aaa', 'k': 2}
    print(f'Test 3 Result:', solution.shortestPath(**inputs3), ' | Expected:', -1)

"""
Notes:
    -
"""
