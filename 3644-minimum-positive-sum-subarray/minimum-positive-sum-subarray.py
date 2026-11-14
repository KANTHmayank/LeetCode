class Solution:

    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # prefixSum = [0] * (len(nums) + 1)
        # prefixSum[0] = 0
        # for i in range(len(nums)):
        #     prefixSum[i + 1] = prefixSum[i] + nums[i]

        # def rangeSum(prefixSum: List[int], a:int, b:int):
        #     return prefixSum[b + 1] - prefixSum[a]

        minSum = float('inf')
        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                if(j - i + 1 > r):
                    break
                if(j - i + 1 >= l and currSum  > 0):
                    # if rangeSum(prefixSum, i, j) > 0:
                    minSum = min(currSum, minSum)
        return minSum if minSum != float('inf') else -1