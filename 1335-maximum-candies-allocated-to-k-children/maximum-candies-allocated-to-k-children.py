class Solution:
    def canAllocate(self, candies: list[int], k: int, x: int) -> bool:
        children = 0
        for i in range(len(candies)):
            if (candies[i] >= x):
                children  += candies[i] // x
            else:
                continue
        return children >= k

    def maximumCandies(self, candies: list[int], k: int) -> int:
        if (sum(candies) < k):
            return 0
        
        l = 1
        h = max(candies)
        ans = 1
        while(l <= h):
            mid = (l + h)//2
            if (self.canAllocate(candies, k, mid)):
                ans = mid
                l = mid + 1
            else:
                h = mid - 1

        return ans