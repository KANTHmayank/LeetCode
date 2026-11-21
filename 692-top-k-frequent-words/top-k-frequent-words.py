class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __lt__(self, other):
        if self.first != other.first:
            return self.first < other.first
        return self.second > other.second
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = {}
        for i in words:
            freq[i]  = freq.get(i, 0) + 1
        h =[]
        for key,value in freq.items():
            if len(h) < k:
                heapq.heappush(h, Pair(value, key))

            elif Pair(value,key) > h[0]:
                heapq.heapreplace(h, Pair(value, key))

        ans = []
        while h:
            ans.append(heapq.heappop(h).second)
        return ans[::-1]
