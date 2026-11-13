class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        low = 0
        count = 0
        res = 0
        f = {}
        for high in range(len(fruits)):

            f[fruits[high]] = f.get(fruits[high], 0) + 1

            
            while(len(f) > 2):
                f[fruits[low]] = f.get(fruits[low] , 0) - 1
                if f[fruits[low]] == 0:
                    f.pop(fruits[low])
                low += 1
                
            count = high - low + 1
            res = max(res, count)
                # low += 1
        return res
