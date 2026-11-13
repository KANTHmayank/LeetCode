class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        # low = 0
        # sum_max = 0
        # f = {}
        # prefix_sum = [0]*(len(nums) + 1)
        # prefix_sum[0] = 0
        # for i in range(len(nums)):
        #     prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        # for high in range(len(nums)):
        #     if(nums[high] in f):
        #         low = max(low, f[nums[high]] + 1)

        #     f[nums[high]] = high
        #     sum_max = max(sum_max, prefix_sum[high + 1] - prefix_sum[low])
        # return sum_max


        low = 0
        current_sum = 0
        max_sum = 0
        seen = set()
        for high in range(len(nums)):
            while nums[high] in seen:
                seen.remove(nums[low])
                current_sum -= nums[low]
                low += 1
            
            seen.add(nums[high])
            current_sum += nums[high]
            max_sum = max(max_sum, current_sum)
        return max_sum