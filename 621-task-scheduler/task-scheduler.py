class Pair:
    def __init__(self, first, second):
        self.first = first    # remaining count
        self.second = second  # character

    def __lt__(self, other):
        return self.first > other.first 
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = {}
        for i in tasks:
            freq[i]= freq.get(i,0) + 1

        h = []
        res = []
        for key,value in freq.items():
            heapq.heappush(h, Pair(value,key))

        last = {}
        time = 0
        while h:
            # if not res:
            #     p = heapq.heappop(h)
            #     res.append(p.second)
            #     p.first -=1
            #     if p.first > 0:
            #         heapq.heappush(h, p)

            skipped = []
            p = heapq.heappop(h)
            # start = max(0, len(res) - n)
            
            while h and p.second in last and time - last[p.second] <= n:
                skipped.append(p)
                p = heapq.heappop(h)

            # skipped.append(p)

            if p.second not in last or time - last[p.second] > n:
                last[p.second] = time
                time += 1
                p.first -= 1
                if p.first > 0:
                    heapq.heappush(h, p)
                for i in skipped:
                    heapq.heappush(h, i)
            else:
                time += 1
                heapq.heappush(h, p)
                for i in skipped:
                    heapq.heappush(h, i)

        return time
            
                
            