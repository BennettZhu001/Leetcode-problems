# problem 973

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            distance_square = point[0] ** 2 + point[1] ** 2
            if len(heap) < k:
                heapq.heappush(heap, (-distance_square, point))
            elif -distance_square >= heap[0][0]:
                heapq.heapreplace(heap, (-distance_square, point))
        k_points = [element[1] for element in heap]

        return k_points
