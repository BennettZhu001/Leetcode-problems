# 215


# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?


# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # first build a min-heap of size k based on the first k elements in nums
        # then iterate over the rest of the nums and compare it to the smallest number in the min-heap
        # if it is bigger than the smallest number in the min-heap, replace the smallest one with the new number
        # and heapify the newly inserted heap.
        # return the smallest number after iterating all the nums
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]


# to build a min heap, you simply start with a list and use heapq. operation on it.
# use heapq.heappush(heap, new) to push elements into the heap
# use heapq.heapreplace(heap, new) to replace the heap[0] by new
# and remain the size of the heap.
# return heap[0]


# time complexity is O(k + n log k )
# space complexity is O(k)
