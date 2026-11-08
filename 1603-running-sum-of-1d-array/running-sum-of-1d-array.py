class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        # runSum = []
        # runSum[0] = nums[0]
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums