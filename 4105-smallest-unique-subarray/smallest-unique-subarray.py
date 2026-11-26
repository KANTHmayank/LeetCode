import math
class Solution:
    def check(self,nums: List[int], size:int, base:int):
        n = len(nums)
        MOD = 10**9 + 7
        count = {}
        p = pow(base, size - 1, MOD)

        i =0
        j = 0
        hash = 0
        while j < n:
            
            hash = (hash * base + nums[j]) % MOD

            if j-i+1 < size:
                j += 1
            else:
                count[hash] = count.get(hash,0) + 1
                hash = (hash - nums[i]*p) % MOD
                i += 1
                j += 1
        return any(v == 1 for v in count.values())

    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        base = max(nums) + 1
        l = 1
        h = n
        res = -1
        while l<=h:
            mid = (l+h)//2

            if self.check(nums, mid, base):
                res = mid
                h = mid - 1
            else:
                l = mid + 1
        return res
        