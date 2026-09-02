# 347.


# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build a dictionary to count each number's frequency with a dictionary
        # Keep the k most frequent numbers in a heap.

        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        heap = []

        for num in frequency:
            if len(heap) < k:
                heapq.heappush(heap, (frequency[num], num))
            elif frequency[num] >= heap[0][0]:
                heapq.heapreplace(heap, (frequency[num], num))

        return [element[1] for element in heap]
