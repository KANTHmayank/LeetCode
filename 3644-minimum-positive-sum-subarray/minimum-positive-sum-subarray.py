class Solution:

    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        prefixSum = [0] * (len(nums) + 1)
        prefixSum[0] = 0
        for i in range(len(nums)):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        def rangeSum(prefixSum: List[int], a:int, b:int):
            return prefixSum[b + 1] - prefixSum[a]

        minSum = float('inf')
        for i in range(len(nums)):
            
            for j in range(i, len(nums)):
                if(j - i + 1 > r):
                    break
                if(j - i + 1 >= l):
                    if rangeSum(prefixSum, i, j) > 0:
                        minSum = min(minSum, rangeSum(prefixSum, i, j))
        return minSum if minSum != float('inf') else -1