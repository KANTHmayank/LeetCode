import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # return heapq.nlargest(k,nums)[-1]

        h = []

        for i in nums[:k]:
            heapq.heappush(h, i)

        for i in nums[k:]:
            if i > h[0]:
                heapq.heapreplace(h, i)
        return h[0]