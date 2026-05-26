"""
Problem:
    Count the Number of Special Characters I
Link:
    https://leetcode.com/problems/count-the-number-of-special-characters-i/
Difficulty:
    Easy
Topics:
    Hash Table, String
"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper = set()
        lower = set()

        for letter in word:
            if letter.isupper():
                upper.add(letter.lower())
            else:
                lower.add(letter)

        specialChars = upper & lower
        
        return len(specialChars)
    
if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: word = "aaAbcBC"  |  Expected Output: 3
    testcase1 = "aaAbcBC"
    print(f'Test 1 Result:', solution.numberOfSpecialChars(testcase1))

    # Example Input: word = "abc"  |  Expected Output: 0
    testcase2 = "abc"
    print(f'Test 2 Result:', solution.numberOfSpecialChars(testcase2))

    # Example Input: word = "abBCab"  |  Expected Output: 1
    testcase3 = "abBCab"
    print(f'Test 3 Result:', solution.numberOfSpecialChars(testcase3))


"""
Approach 1:
    - Store lowercase and uppercase characters in separate sets
    - Normalize uppercase letters to lowercase
    - Use set intersection to find common characters
Issue:
    -
Final Approach:
    - Approach 1 passed on LeetCode with
        Runtime 0ms Beats 100.00%
        Memory 19.27MB Beats 64.16%

Complexity:
    Time: O(n)
    Space: O(1) since the charset is fixed (a-z, A-Z)
Notes: 
    - Reviewed space complexity analysis separately to better understand constant-space scenarios. 
    - For this problem I had to search about set comparisons and if I was able to create a set
        through conditions, so far I had only used it on lists to get unique values.
"""
