# problem 621. Task scheduler

"""
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n.
Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

Return the minimum number of CPU intervals required to complete all tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.



Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100


"""

import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count frequency of each letter.
        # find the largest frequency L.
        # return (L-1)*(n+1) + 1 = L(n+1) - n it takes
        # L(n+1) - n - L = L n - n = (L - 1) n

        frequency_dict = {}
        for task in tasks:
            if task not in frequency_dict:
                frequency_dict[task] = 1
            else:
                frequency_dict[task] += 1

        # build a max heap by a min heap with negative value.
        heap = [-frequency_dict[task] for task in frequency_dict]
        heapq.heapify(heap)

        intervals = 0

        while heap:
            # pop up to n+1 highest-frequency tasks
            counter = 0
            remaining = []
            while heap and counter < n + 1:
                counter += 1

                # since we use negative value in the heap, we
                # add one to move it towards zero.
                remaining.append(heapq.heappop(heap) + 1)

            while remaining:
                decreased_freq = remaining.pop()
                if decreased_freq != 0:
                    heapq.heappush(heap, decreased_freq)

            if heap:
                intervals += n + 1
            else:
                intervals += counter

        return intervals


def main():
    test_cases = [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "C", "A", "B", "D", "B"], 1, 6),
        (["A", "A", "A", "B", "B", "B"], 3, 10),
        (["A", "B"], 3, 2),
        (["A", "A", "A"], 0, 3),
        (["A", "A", "A", "A"], 2, 10),
        (["A", "A", "A", "B", "B", "B", "C"], 2, 8),
        (["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "D"], 2, 12),
        (["A", "A", "B", "B", "C", "C", "D", "D"], 3, 8),
        (["A", "B", "C", "D", "E"], 100, 5),
    ]

    solution = Solution()
    for tasks, n, expected in test_cases:
        actual = solution.leastInterval(tasks, n)
        assert actual == expected, (
            f"tasks={tasks}, n={n}: expected {expected}, got {actual}"
        )

    print("All task scheduler tests passed!")


if __name__ == "__main__":
    main()
