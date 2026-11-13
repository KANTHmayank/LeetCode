class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        low = 0
        sum_max = 0
        f = {}
        for high in range(len(nums)):
            if(nums[high] in f):
                low = max(low, f[nums[high]] + 1)

            f[nums[high]] = high
            sum_max = max(sum_max, sum(nums[low:high + 1]))
        return sum_max