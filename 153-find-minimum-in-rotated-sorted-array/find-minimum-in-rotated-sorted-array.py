class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l = 0
        h = n - 1
        while l <= h:
            guess = (l + h)//2
            if nums[guess] > nums[n -1]:
                l =guess + 1
            else:
                res = guess
                h = guess - 1
        return nums[res]