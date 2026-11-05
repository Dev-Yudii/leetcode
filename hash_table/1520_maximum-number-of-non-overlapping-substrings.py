"""
This problem was extracted on 2026-11-05 11:19 (UTC+0) from LeetCode at https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/.
You can check the full problem description there.
Problem Title:
    Maximum Number of Non-Overlapping Substrings
Difficulty:
    Hard
Tags:
    Hash Table, String, Greedy, Sorting
"""

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: s = "adefaddaccc"  |  Expected Output: ["e","f","ccc"]
    inputs1 = {'s': 'adefaddaccc'}
    print(f'Test 1 Result:', solution.maxNumOfSubstrings(**inputs1), ' | Expected:', ['e', 'f', 'ccc'])

    # Example Input: s = "abbaccd"  |  Expected Output: ["d","bb","cc"]
    inputs2 = {'s': 'abbaccd'}
    print(f'Test 2 Result:', solution.maxNumOfSubstrings(**inputs2), ' | Expected:', ['d', 'bb', 'cc'])

"""
Notes:
    -
"""
