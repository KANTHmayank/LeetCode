# class Pair:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second

#     def __lt__(self, other):
#         if self.first != other.first:
#             return self.first> other.first
#         return self.second < other.second
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        h = []
        
        reach = startFuel
        count = 0
        stations.sort(key = lambda x: (x[0], -x[1]))
        stations.append([target,0])

        for i,j in stations:
            while reach < i:
                if not h:
                    return -1
                p = -heapq.heappop(h)
                reach += p
                count += 1
            
            heapq.heappush(h, -j)

        return count
        


        