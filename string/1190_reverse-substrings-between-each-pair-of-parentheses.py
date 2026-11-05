"""
This problem was extracted on 2026-11-05 11:22 (UTC+0) from LeetCode at https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/.
You can check the full problem description there.
Problem Title:
    Reverse Substrings Between Each Pair of Parentheses
Difficulty:
    Medium
Tags:
    String, Stack, Bracket Sequences
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: s = "(abcd)"  |  Expected Output: "dcba"
    inputs1 = {'s': '(abcd)'}
    print(f'Test 1 Result:', solution.reverseParentheses(**inputs1), ' | Expected:', 'dcba')

    # Example Input: s = "(u(love)i)"  |  Expected Output: "iloveu"
    inputs2 = {'s': '(u(love)i)'}
    print(f'Test 2 Result:', solution.reverseParentheses(**inputs2), ' | Expected:', 'iloveu')

    # Example Input: s = "(ed(et(oc))el)"  |  Expected Output: "leetcode"
    inputs3 = {'s': '(ed(et(oc))el)'}
    print(f'Test 3 Result:', solution.reverseParentheses(**inputs3), ' | Expected:', 'leetcode')

"""
Notes:
    -
"""
