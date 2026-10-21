"""
This problem was extracted on 2026-10-04 23:18 (UTC-3) from LeetCode at https://leetcode.com/problems/score-of-parentheses/.
You can check the full problem description there.
Problem Title:
    Score of Parentheses
Difficulty:
    Medium
Tags:
    String, Stack, Bracket Sequences
"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: s = "()"  |  Expected Output: 1
    inputs1 = {}
    exec('s = "()"', {}, inputs1)
    print(f'Test 1 Result:', solution.scoreOfParentheses(**inputs1), ' | Expected:', '1')

    # Example Input: s = "(())"  |  Expected Output: 2
    inputs2 = {}
    exec('s = "(())"', {}, inputs2)
    print(f'Test 2 Result:', solution.scoreOfParentheses(**inputs2), ' | Expected:', '2')

    # Example Input: s = "()()"  |  Expected Output: 2
    inputs3 = {}
    exec('s = "()()"', {}, inputs3)
    print(f'Test 3 Result:', solution.scoreOfParentheses(**inputs3), ' | Expected:', '2')

"""
Notes:
    -
"""
