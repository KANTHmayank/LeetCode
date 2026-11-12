class Solution:
    def allDistributed(self, n: int, quantities: list[int], x: int) -> bool:
        # sumQuantities = sum(quantities)
        stores = 0
        for i in range(len(quantities)):
            stores += (quantities[i] + x - 1) // x

        return stores <= n
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        l = 1
        h = max(quantities)
        ans = h
        while(l <= h):
            mid = (l + h) // 2
            if (self.allDistributed(n, quantities, mid)):
                ans = mid
                h = mid  - 1
            else:
                l = mid + 1
        return ans