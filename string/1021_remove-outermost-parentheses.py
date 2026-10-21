"""
This problem was extracted on 2026-10-08 19:01 (UTC-3) from LeetCode at https://leetcode.com/problems/remove-outermost-parentheses/.
You can check the full problem description there.
Problem Title:
    Remove Outermost Parentheses
Difficulty:
    Easy
Tags:
    String, Stack, Bracket Sequences
"""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: s = "(()())(())"  |  Expected Output: "()()()"
    inputs1 = {}
    exec('s = "(()())(())"', {}, inputs1)
    print(f'Test 1 Result:', solution.removeOuterParentheses(**inputs1), ' | Expected:', '"()()()"')

    # Example Input: s = "(()())(())(()(()))"  |  Expected Output: "()()()()(())"
    inputs2 = {}
    exec('s = "(()())(())(()(()))"', {}, inputs2)
    print(f'Test 2 Result:', solution.removeOuterParentheses(**inputs2), ' | Expected:', '"()()()()(())"')

    # Example Input: s = "()()"  |  Expected Output: ""
    inputs3 = {}
    exec('s = "()()"', {}, inputs3)
    print(f'Test 3 Result:', solution.removeOuterParentheses(**inputs3), ' | Expected:', '""')

"""
Notes:
    -
"""
