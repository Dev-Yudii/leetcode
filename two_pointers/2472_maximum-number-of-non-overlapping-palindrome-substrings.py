"""
This problem was extracted on 2026-11-05 11:18 (UTC+0) from LeetCode at https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/.
You can check the full problem description there.
Problem Title:
    Maximum Number of Non-overlapping Palindrome Substrings
Difficulty:
    Hard
Tags:
    Two Pointers, String, Dynamic Programming, Greedy
"""

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: s = "abaccdbbd", k = 3  |  Expected Output: 2
    inputs1 = {'s': 'abaccdbbd', 'k': 3}
    print(f'Test 1 Result:', solution.maxPalindromes(**inputs1), ' | Expected:', 2)

    # Example Input: s = "adbcda", k = 2  |  Expected Output: 0
    inputs2 = {'s': 'adbcda', 'k': 2}
    print(f'Test 2 Result:', solution.maxPalindromes(**inputs2), ' | Expected:', 0)

"""
Notes:
    -
"""
