# problem_53.py

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

from init import *


class Solution:
    def maxSubArray_DP_recursion(self, nums: List[int]) -> int:
        # This is a function of using DP with memoization to solve the problem;
        if not nums:
            return None
        n = len(nums)
        memo = {}
        memo[n - 1] = (nums[n - 1], nums[n - 1])

        def dp(i):
            # i is an integer between 0 and n-1
            if i in memo:
                return memo[i]

            temp = dp(i + 1)
            max_subarray_start_from_i_sum = max(nums[i], nums[i] + temp[1])

            max_subarray_sum = max(max_subarray_start_from_i_sum, temp[0])

            memo[i] = (max_subarray_sum, max_subarray_start_from_i_sum)
            return memo[i]

        return dp(0)[0]

    def maxSubArray_DP_bottom_up(self, nums: List[int]) -> int:
        if not nums:
            return None
        n = len(nums)
        max_subarray_sum = [None] * n
        max_subarray_start_from_i_sum = [None] * n

        max_subarray_sum[n - 1] = nums[n - 1]
        max_subarray_start_from_i_sum[n - 1] = nums[n - 1]

        for i in reversed(range(n - 1)):
            max_subarray_start_from_i_sum[i] = max(
                nums[i], nums[i] + max_subarray_start_from_i_sum[i + 1]
            )
            max_subarray_sum[i] = max(
                max_subarray_sum[i + 1], max_subarray_start_from_i_sum[i]
            )
        return max_subarray_sum[0]

    # Remark on Divide and Conquer.
    # Introduction to algorithm book used this problem in the divide and conquer illustration.
    # It seems like we can include more information/elements in the recursion in order to make the merge
    # step simpler with a little bit more space each recursion(O(log n) space for the whole algorithm).
    # The price is very cheap yet the reward might be considerable.
    #

    def maxSubArray_divide_and_conquer(self, nums) -> tuple:
        # we return a tuple of four elements: largest sum of subarray, prefix, suffix, total sum
        if not nums:
            return None
        n = len(nums)
        if n == 1:
            return (nums[0], nums[0], nums[0], nums[0])
        elif n == 2:
            total_sum = nums[0] + nums[1]
            prefix = max(nums[0], total_sum)
            suffix = max(nums[1], total_sum)
            return (max(prefix, suffix), prefix, suffix, total_sum)
        else:
            mid = n // 2
            first_half = self.maxSubArray_divide_and_conquer(nums[:mid])
            second_half = self.maxSubArray_divide_and_conquer(nums[mid:])

            prefix = max(first_half[1], first_half[3] + second_half[1])
            suffix = max(second_half[2], second_half[3] + first_half[2])
            total_sum = first_half[3] + second_half[3]
            subarray = max(
                first_half[0], second_half[0], first_half[2] + second_half[1]
            )
            return subarray, prefix, suffix, total_sum
