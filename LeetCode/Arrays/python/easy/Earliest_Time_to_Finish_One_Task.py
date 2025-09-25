# Earliest Time to Finish One Task

# You are given a 2D integer array tasks where tasks[i] = [si, ti].
# Each [si, ti] in tasks represents a task with start time si that takes ti units of time to finish.
# Return the earliest time at which at least one task is finished.

# Example 1:

# Input: tasks = [[1,6],[2,3]]
# Output: 5
# Explanation:
# The first task starts at time t = 1 and finishes at time 1 + 6 = 7. The second task finishes at time 2 + 3 = 5. You can finish one task at time 5.

# Example 2:

# Input: tasks = [[100,100],[100,100],[100,100]]
# Output: 200
# Explanation:
# All three tasks finish at time 100 + 100 = 200.


class Solution:
    def earliestTime(self, tasks: list[list[int]]) -> int:

        result: list[int] = []

        for i in tasks:
            result.append(i[0] + i[1])

        return min(result)


obj = Solution()
# tasks = [[1, 6], [2, 3]]
tasks = [[100, 100], [100, 100], [100, 100]]
print(obj.earliestTime(tasks))
