"""
This problem was extracted on 2026-11-05 11:14 (UTC+0) from LeetCode at https://leetcode.com/problems/distinct-subsequences/.
You can check the full problem description there.
Problem Title:
    Distinct Subsequences
Difficulty:
    Hard
Tags:
    String, Dynamic Programming
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: s = "rabbbit", t = "rabbit"  |  Expected Output: 3
    inputs1 = {'s': 'rabbbit', 't': 'rabbit'}
    print(f'Test 1 Result:', solution.numDistinct(**inputs1), ' | Expected:', 3)

    # Example Input: s = "babgbag", t = "bag"  |  Expected Output: 5
    inputs2 = {'s': 'babgbag', 't': 'bag'}
    print(f'Test 2 Result:', solution.numDistinct(**inputs2), ' | Expected:', 5)

"""
Notes:
    -
"""
