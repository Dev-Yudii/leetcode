"""
Problem:
    Destroying Asteroids
Link:
    https://leetcode.com/problems/destroying-asteroids/
Difficulty:
    Medium
Topics:
    Array, Greedy, Sorting
"""
from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if  mass >= asteroid:
                mass += asteroid
            else:
                return False
            
        return True

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: mass = 10, asteroids = [3,9,19,5,21]  |  Expected Output: true
    inputs1 = {}
    exec("mass = 10 ; asteroids = [3,9,19,5,21]", {}, inputs1)
    print(f'Test 1 Result:', solution.asteroidsDestroyed(**inputs1), ' | Expected:', 'True')

    # Example Input: mass = 5, asteroids = [4,9,23,4]  |  Expected Output: false
    inputs2 = {}
    exec("mass = 5 ; asteroids = [4,9,23,4]", {}, inputs2)
    print(f'Test 2 Result:', solution.asteroidsDestroyed(**inputs2), ' | Expected:', 'False')

"""
Approach 1:
    - Order the list to ascending
    - For every asteroid on array lower or equal to mass, sum it to the mass
    - If asteroid is higher than mass return False, else all the list goes through return True
Issue:
    - 
Final Approach:
    - Approach - passed on LeetCode with
        Runtime 80 ms Beats 35.89%
        Memory 34.00 MB Beats 53.36%
Complexity:
    - Time: O(N log N)
    - Space: O(N)
Notes:
    - 
"""
