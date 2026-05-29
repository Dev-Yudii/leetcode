"""
Problem:
    Longest Common Suffix Queries
Link:
    https://leetcode.com/problems/longest-common-suffix-queries/
Difficulty:
    Hard
Topics:
    Array, String, Trie
"""
from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, key):
        curr = self.root # Initializes at first index

        for c in key: # Runs through every letter
            index = ord(c) - ord('a') # Return the position the letter belongs to
            if curr.children[index] is None: # If it's empty
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        
        curr.isLeaf = True

    def search(self, key):
        curr = self.root

        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False

            curr = curr.children[index]
        
        return curr.isLeaf
    
    def is_prefix(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
        
            if curr.children[index] is None:
                return False
            
            curr = curr.children[index]
        
        return True

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        for words in wordsQuery:
            words

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]  |  Expected Output: [1,1,1]
    testcase1 = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]
    print(f'Test 1 Result:', solution.stringIndices(testcase1))

    # Example Input: wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]  |  Expected Output: [2,0,2]
    testcase2 = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]
    print(f'Test 2 Result:', solution.stringIndices(testcase2))


"""
Approach 1:
    - Invert all Strings
    - Apply Trie algorithm
Issue:
    - 
Final Approach:
    - Approach - passed on LeetCode with
        Runtime - ms Beats -%
        Memory - MB Beats -%
Complexity:
    Time: O()
    Space: O()
Notes:
    - I usually don't look at topics when doing leetcode, but now it's instantly shown when the script
        runs. So I saw this topic I have no knowledge of, `Trie`.
        Had to search about it, and on https://www.geeksforgeeks.org/dsa/trie-insert-and-search/
        I found this: "We can efficiently do prefix search (or auto-complete) with Trie."
        So maybe first approach is to invert the words and try using it. But it also says it uses a lot
        of memory, every node points to every letter, so 26 pointers for each node. Need to be aware of it
"""
