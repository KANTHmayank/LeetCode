import math
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __lt__(self, other):
        if self.first != other.first:
            return self.first > other.first
        
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        h = []
        for x,y in points:
            d = x*x + y*y

            if len(h) < k:
                heapq.heappush(h, Pair(d, [x,y]))
            elif d < h[0].first:
                heapq.heapreplace(h, Pair(d, [x,y]))

        ans= []
        while h:
            ans.append(heapq.heappop(h).second)
        return ans
        
    