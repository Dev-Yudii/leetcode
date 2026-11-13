"""
This problem was extracted on 2026-11-13 07:59 (UTC+0) from LeetCode at https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/.
You can check the full problem description there.
Problem Title:
    Count Non-Decreasing Subarrays After K Operations
Difficulty:
    Hard
Tags:
    Array, Stack, Segment Tree, Queue, Sliding Window, Monotonic Stack, Monotonic Queue
"""

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: nums = [6,3,1,2,4,4], k = 7  |  Expected Output: 17
    inputs1 = {'nums': [6, 3, 1, 2, 4, 4], 'k': 7}
    print(f'Test 1 Result:', solution.countNonDecreasingSubarrays(**inputs1), ' | Expected:', 17)

    # Example Input: nums = [6,3,1,3,6], k = 4  |  Expected Output: 12
    inputs2 = {'nums': [6, 3, 1, 3, 6], 'k': 4}
    print(f'Test 2 Result:', solution.countNonDecreasingSubarrays(**inputs2), ' | Expected:', 12)

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
