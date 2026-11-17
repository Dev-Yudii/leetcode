"""
This problem was extracted on 2026-11-17 09:14 (UTC+0) from LeetCode at https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/.
You can check the full problem description there.
Problem Title:
    Minimum Changes to Make K Semi-palindromes
Difficulty:
    Hard
Tags:
    Two Pointers, String, Dynamic Programming
"""

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: s = "abcac", k = 2  |  Expected Output: 1
    inputs1 = {'s': 'abcac', 'k': 2}
    print(f'Test 1 Result:', solution.minimumChanges(**inputs1), ' | Expected:', 1)

    # Example Input: s = "abcdef", k = 2  |  Expected Output: 2
    inputs2 = {'s': 'abcdef', 'k': 2}
    print(f'Test 2 Result:', solution.minimumChanges(**inputs2), ' | Expected:', 2)

    # Example Input: s = "aabbaa", k = 3  |  Expected Output: 0
    inputs3 = {'s': 'aabbaa', 'k': 3}
    print(f'Test 3 Result:', solution.minimumChanges(**inputs3), ' | Expected:', 0)

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
