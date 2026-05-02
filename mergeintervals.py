intervals = [[1,3],[4,5],[2,6],[8,10],[15,18]]

def mergeIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
#    print(intervals)
    merged = []

    for i in intervals:
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1], i[1])

    return merged

print(mergeIntervals(intervals))
