class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __lt__(self, other):
        if self.first != other.first:
            return self.first > other.first
        return self.second > other.second
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        # seat = 0
        freq = {}
        for i in s:
            freq[i] = freq.get(i,0) + 1

        h = []
        for key,value in freq.items():
            heapq.heappush(h, Pair(value, key))

        # seat = 0
        while h:
            p = heapq.heappop(h)
            if not res or res[-1] != p.second:
                res.append(p.second)
                # seat += 1
                p.first -= 1
            

                if p.first  > 0:
                    heapq.heappush(h, p)

            else:
                if not h:
                    return ""
                p1 = heapq.heappop(h)
                res.append(p1.second)
                # seat += 1
                p1.first -= 1

                if p1.first > 0:
                    heapq.heappush(h, p1)

                heapq.heappush(h, p)

        return "".join(res)
