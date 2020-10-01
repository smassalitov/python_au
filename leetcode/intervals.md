# Intervals
+ [Non-overlapping Intervals](#Non-overlapping-Intervals)
+ [Merge Intervals](#Merge-Intervals)
+ [Insert Interval](#Insert-Interval)
## Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/
```python
class Solution:
    def eraseOverlapIntervals(self, intervals):
            if len(intervals) <= 1:
                return 0
            intervals.sort(key=lambda element: element[1])
            previous_element = float("-inf")
            result = 0
            for i in intervals:
                if i[0] >= previous_element:
                    previous_element = i[1]
                else:
                    result += 1
            return result

```
## Merge Intervals
https://leetcode.com/problems/merge-intervals/
```python
class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda element: element[0])
        result = []
        start_interval = intervals[0]
        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            if current_interval[0] > start_interval[1]:
                result.append(start_interval)
                start_interval = current_interval
            else:
                start_interval[1] = max(start_interval[1], current_interval[1])
        result.append(start_interval)
        return result

```
## Insert Interval
https://leetcode.com/problems/insert-interval/
```python
class Solution:
    def insert(self, intervals, new):
        merged = []
        count = 0
        if len(intervals) == 0:
            return [new]
        for curr in intervals:
            if new[0] > curr[1]:
                merged.append(curr)
            elif curr[0] > new[1]:
                break
            else:
                new[0] = min(new[0], curr[0])
                new[1] = max(new[1], curr[1])
            count += 1
        merged.append(new)
        if count < len(intervals):
            return merged + intervals[count:]
        else:
            return merged

```
