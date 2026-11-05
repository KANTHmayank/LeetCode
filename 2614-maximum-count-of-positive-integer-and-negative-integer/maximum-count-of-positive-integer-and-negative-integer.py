class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        firstNonNeg = len(nums)
        while(left <= right):
            mid = (left + right)//2
            if(nums[mid] >= 0):
                firstNonNeg = mid
                right = mid - 1
                
            else:
                left = mid + 1

        left = 0
        right = len(nums) - 1
        firstPos = len(nums)
        while(left <= right):
            mid = (left + right)//2
            if(nums[mid] > 0):
                firstPos = mid
                right = mid - 1
            else:
                left = mid + 1

        posCount = len(nums) - firstPos
        negCount = firstNonNeg
        return max(posCount, negCount)
