# 1099 Two sum less than K.


"""

### Problem Statement

  Given an array nums of integers and an integer
  k, return the maximum sum such that there
  exists i < j with nums[i] + nums[j] = sum and
  sum < k. If no such i, j exists, return -1.
  Example 1:

  • Input: nums = [34, 23, 1, 24, 75, 33, 54, 8],
  k = 60
  • Output: 58
  • Explanation: We can pick 34 and 24 to sum to
  58 (58 < 60).
  Example 2:

  • Input: nums = [10, 20, 30], k = 15
  • Output: -1
  • Explanation: In this case, it is impossible
  to find a pair with sum less than 15.




"""


def twosum_less_than(nums, k):
    nums.sort()
    # Two pointers
    n = len(nums)
    left_pointer = 0
    right_pointer = n - 1
    max_sum = -1

    while left_pointer < right_pointer:
        two_sum = nums[left_pointer] + nums[right_pointer]
        if two_sum < k:
            max_sum = max(max_sum, two_sum)
            left_pointer += 1
        else:
            right_pointer -= 1
    return max_sum


def twosum_less_than_equal_two(nums, k):
    nums.sort()
    # Two pointers
    n = len(nums)
    left_pointer = 0
    right_pointer = n - 1
    max_sum = -1

    while left_pointer < right_pointer:
        two_sum = nums[left_pointer] + nums[right_pointer]
        if two_sum == k:
            return k
        elif two_sum < k:
            max_sum = max(max_sum, two_sum)
            left_pointer += 1
        else:
            right_pointer -= 1
    return max_sum
