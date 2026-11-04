"""
This problem was extracted on 2026-10-27 10:27 (UTC-3) from LeetCode at https://leetcode.com/problems/create-grid-with-exactly-one-path/.
You can check the full problem description there.
Problem Title:
    Create Grid With Exactly One Path
Difficulty:
    Easy
Tags:
    
"""

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        print('hello world')
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: m = 2, n = 3  |  Expected Output: ["..#","#.."]
    inputs1 = {'m': 2, 'n': 3}
    print(f'Test 1 Result:', solution.createGrid(**inputs1), ' | Expected:', ['..#', '#..'])

    # Example Input: m = 3, n = 3  |  Expected Output: ["..#","#..","##."]
    inputs2 = {'m': 3, 'n': 3}
    print(f'Test 2 Result:', solution.createGrid(**inputs2), ' | Expected:', ['..#', '#..', '##.'])

    # Example Input: m = 1, n = 4  |  Expected Output: ["...."]
    inputs3 = {'m': 1, 'n': 4}
    print(f'Test 3 Result:', solution.createGrid(**inputs3), ' | Expected:', ['....'])

"""
Notes:
    -
"""
