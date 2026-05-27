"""
Problem:
    Count the Number of Special Characters II
Link:
    https://leetcode.com/problems/count-the-number-of-special-characters-ii/
Difficulty:
    Medium
Topics:
    Hash Table, String
"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper = set()
        lower = set()
        invalid = set()

        for letter in word:
            if letter not in invalid:
                if letter.islower():
                    if letter in upper:
                        invalid.add(letter)
                    lower.add(letter)
                else:
                    upper.add(letter.lower())

        valid_lower = lower - invalid
        specialChars = upper & valid_lower
        
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

    # Example Input: word = "AbBCab"  |  Expected Output: 0
    testcase3 = "AbBCab"
    print(f'Test 3 Result:', solution.numberOfSpecialChars(testcase3))


"""
Approach 1:
    - Store lowercase and uppercase characters in separate sets, create another set for invalid letters.
    - If a lowercase letter appears and it's already on upper set, it goes to invalid set
    - Normalize uppercase letters to lowercase
    - Use set difference to find valid lower values
    - Use set intersection to find common characters
Issue:
    - 
Final Approach:
    - Approach - passed on LeetCode with
        Runtime - 255 ms Beats 58.82%
        Memory - 21.59 Beats 47.06%
Complexity:
    Time: O(n)
    Space: O(1) since the charset is fixed (a-z, A-Z)
Notes:
    - Used yesterday's answer and added the new problem conditions
"""
