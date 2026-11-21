class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # while len(stones) >1:
        #     h = []
        #     for i in range(len(stones)):
        #         if i < 2:
        #             heapq.heappush(h, stones[i])
        #         elif stones[i] > h[0]:
        #             heapq.heapreplace(h, stones[i])

        #     stones.remove(h[0])
        #     stones.remove(h[1])

        #     if h[0] != h[1]:
        #         stones.append(abs(h[0] - h[1]))
        # return stones[0] if stones else 0

        h = [-s for s in stones]
        heapq.heapify(h)

        while len(h) > 1:
            a= -heapq.heappop(h)
            b =  -heapq.heappop(h)

            if a != b:
                heapq.heappush(h, b-a)

        return -h[0] if h else 0
