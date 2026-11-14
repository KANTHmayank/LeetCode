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
            # minSum = float('inf')
            for length in range(l,r+1):
                j = i + length - 1
                if j >= len(nums):
                    break
                sum = prefixSum[j+1] - prefixSum[i]
                # currSum += nums[j]
                # if(j - i + 1 > r):
                #     break
                if(sum  > 0):
                    # if rangeSum(prefixSum, i, j) > 0:
                    minSum = min(minSum, sum)
        return minSum if minSum != float('inf') else -1