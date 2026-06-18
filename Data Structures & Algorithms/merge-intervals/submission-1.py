class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        merged = []

        prev = intervals[0]

        merged.append(prev)

        for i in range(1, len(intervals)):

            if intervals[i][0] <= prev[1]:
                end = prev[1] if prev[1] >= intervals[i][1] else intervals[i][1]
                merged.pop()
                new = [prev[0], end]
                merged.append(new)
                prev = new
            else:
                merged.append(intervals[i])
                prev = intervals[i]
        
        return merged
            


