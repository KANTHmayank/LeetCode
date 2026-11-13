class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        low = 0
        sum_max = 0
        f = {}
        prefix_sum = [0]*(len(nums) + 1)
        prefix_sum[0] = 0
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        for high in range(len(nums)):
            if(nums[high] in f):
                low = max(low, f[nums[high]] + 1)

            f[nums[high]] = high
            sum_max = max(sum_max, prefix_sum[high + 1] - prefix_sum[low])
        return sum_max