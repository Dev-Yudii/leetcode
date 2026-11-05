"""
This problem was extracted on 2026-11-05 11:22 (UTC+0) from LeetCode at https://leetcode.com/problems/brace-expansion-ii/.
You can check the full problem description there.
Problem Title:
    Brace Expansion II
Difficulty:
    Hard
Tags:
    Hash Table, String, Backtracking, Stack, Breadth-First Search, Sorting
"""

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: expression = "{a,b}{c,{d,e}}"  |  Expected Output: ["ac","ad","ae","bc","bd","be"]
    inputs1 = {'expression': '{a,b}{c,{d,e}}'}
    print(f'Test 1 Result:', solution.braceExpansionII(**inputs1), ' | Expected:', ['ac', 'ad', 'ae', 'bc', 'bd', 'be'])

    # Example Input: expression = "{{a,z},a{b,c},{ab,z}}"  |  Expected Output: ["a","ab","ac","z"]
    inputs2 = {'expression': '{{a,z},a{b,c},{ab,z}}'}
    print(f'Test 2 Result:', solution.braceExpansionII(**inputs2), ' | Expected:', ['a', 'ab', 'ac', 'z'])

"""
Notes:
    -
"""
