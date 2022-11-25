You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
  
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ans = []
        start = newInterval[0]
        end = newInterval[1]

        i = 0

        while i < len(intervals) and intervals[i][1] < start:
            ans.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= end:
            start = min(start,intervals[i][0])
            end = max(end,intervals[i][1])
            i += 1
        ans.append([start,end])

        while i < len(intervals):
            ans.append(intervals[i])
            i += 1
        return ans
