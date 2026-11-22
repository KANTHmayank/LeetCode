class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __lt__(self, other):
        if self.first != other.first:
            return self.first < other.first
        # return self.second < other.second
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # h= []
        # for i in range(len(profits)):
        #     heapq.heappush(h, Pair(profits[i], capital[i]))

        
        # count = 0

        # if w < min(capital):
        #     return 0
        # while h:
        #     skipped = []
        #     p = heapq.heappop(h)
        #     while h and w < p.second:
        #         skipped.append(p)
        #         print(skipped[0].second)
        #         p = heapq.heappop(h)
            

        #     if w >= p.second:
        #         w += p.first
            
        #         count += 1
        #     for i in skipped:
        #         if w >= i.second:
        #             heapq.heappush(h, i)
        #     if count == k:
        #         return w 
        # return w

        # minHeap = []
        # for i in range(len(profits)):
        #     heapq.heappush(minHeap, Pair(capital[i], profits[i]))

        # count = 0
        # maxHeap = []

        # while count < k:
        #     while minHeap and minHeap[0].first <= w:
        #         p = heapq.heappop(minHeap)
        #         heapq.heappush(maxHeap, Pair(-p.second, p.first))

        #     if not maxHeap:
        #         break

        #     p = heapq.heappop(maxHeap)
        #     w += -p.first
        #     count += 1

        # return w
            
        projects = sorted(zip(capital, profits))   # replaces the capital heap
        n = len(projects)
        h = []          # plain negated ints: C-level comparisons
        i = 0

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(h, -projects[i][1])
                i += 1
            if not h:
                break
            w -= heapq.heappop(h)

        return w