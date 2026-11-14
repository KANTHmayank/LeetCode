from sortedcontainers import SortedList
class Solution:

    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        prefixSum = [0] * (len(nums) + 1)
        prefixSum[0] = 0
        for i in range(len(nums)):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        # def rangeSum(prefixSum: List[int], a:int, b:int):
        #     return prefixSum[b + 1] - prefixSum[a]

        # minSum = float('inf')
        # for i in range(len(nums)):
        #     # minSum = float('inf')
        #     for length in range(l,r+1):
        #         j = i + length - 1
        #         if j >= len(nums):
        #             break
        #         sum = prefixSum[j+1] - prefixSum[i]
        #         # currSum += nums[j]
        #         # if(j - i + 1 > r):
        #         #     break
        #         if(sum  > 0):
        #             # if rangeSum(prefixSum, i, j) > 0:
        #             minSum = min(minSum, sum)
        # return minSum if minSum != float('inf') else -1
        n = len(nums)
        st = SortedList()
        result = float('inf')
        for j in range(l, n+1):
            st.add(prefixSum[j - l])

            if(j -r - 1 >= 0):
                st.remove(prefixSum[j - r -1])
            
            idx = st.bisect_left(prefixSum[j])

            if idx > 0:
                largestBefore = st[idx - 1]
                result = min(result, prefixSum[j] - largestBefore)

        return result if result != float('inf') else -1

