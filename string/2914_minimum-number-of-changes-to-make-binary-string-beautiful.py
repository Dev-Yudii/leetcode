"""
This problem was extracted on 2026-11-18 08:33 (UTC+0) from LeetCode at https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/.
You can check the full problem description there.
Problem Title:
    Minimum Number of Changes to Make Binary String Beautiful
Difficulty:
    Medium
Tags:
    String
"""

class Solution:
    def minChanges(self, s: str) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: s = "1001"  |  Expected Output: 2
    inputs1 = {'s': '1001'}
    print(f'Test 1 Result:', solution.minChanges(**inputs1), ' | Expected:', 2)

    # Example Input: s = "10"  |  Expected Output: 1
    inputs2 = {'s': '10'}
    print(f'Test 2 Result:', solution.minChanges(**inputs2), ' | Expected:', 1)

    # Example Input: s = "0000"  |  Expected Output: 0
    inputs3 = {'s': '0000'}
    print(f'Test 3 Result:', solution.minChanges(**inputs3), ' | Expected:', 0)

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
