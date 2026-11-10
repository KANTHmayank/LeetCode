class Solution:
    def khaSaktaHai(self, piles: list[int], h: int, x: int) -> bool:
        time = 0
        for i in range(len(piles)):
            time += (piles[i] + x - 1) // x
        return True if time <= h else False
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r) // 2
            if (self.khaSaktaHai(piles, h, mid)):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans