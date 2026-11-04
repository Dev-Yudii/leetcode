"""
This problem was extracted on 2026-10-24 17:02 (UTC-3) from LeetCode at https://leetcode.com/problems/count-days-spent-together/.
You can check the full problem description there.
Problem Title:
    Count Days Spent Together
Difficulty:
    Easy
Tags:
    Math, String
"""

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"  |  Expected Output: 3
    inputs1 = {'arriveAlice': '08-15', 'leaveAlice': '08-18', 'arriveBob': '08-16', 'leaveBob': '08-19'}
    print(f'Test 1 Result:', solution.countDaysTogether(**inputs1), ' | Expected:', 3)

    # Example Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"  |  Expected Output: 0
    inputs2 = {'arriveAlice': '10-01', 'leaveAlice': '10-31', 'arriveBob': '11-01', 'leaveBob': '12-31'}
    print(f'Test 2 Result:', solution.countDaysTogether(**inputs2), ' | Expected:', 0)

"""
Notes:
    -
"""
