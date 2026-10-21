"""
This problem was extracted on 2026-10-02 20:18 (UTC-3) from LeetCode at https://leetcode.com/problems/generate-parentheses/.
You can check the full problem description there.
Problem Title:
    Generate Parentheses
Difficulty:
    Medium
Tags:
    String, Dynamic Programming, Backtracking, Bracket Sequences
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: n = 3  |  Expected Output: ["((()))","(()())","(())()","()(())","()()()"]
    inputs1 = {}
    exec('n = 3', {}, inputs1)
    print(f'Test 1 Result:', solution.generateParenthesis(**inputs1), ' | Expected:', '["((()))","(()())","(())()","()(())","()()()"]')

    # Example Input: n = 1  |  Expected Output: ["()"]
    inputs2 = {}
    exec('n = 1', {}, inputs2)
    print(f'Test 2 Result:', solution.generateParenthesis(**inputs2), ' | Expected:', '["()"]')

"""
Notes:
    -
"""
