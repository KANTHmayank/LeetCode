class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # left = 0
        # right = len(nums) - 1
        # while(left <= right):
        #     mid = (left + right)//2
        #     if nums[mid] == target:
        #         return mid
        #     if nums[mid] >= nums[left]:
        #         if target < nums[mid] and target >= nums[left]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     elif nums[mid] < nums[left]:
        #         if target > nums[mid] and target <= nums[right]:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        # return -1

        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left +  right)//2
            if nums[mid] > nums[n - 1]:
                left = mid + 1
            else:
                idx= mid
                right = mid - 1
        
        # divide array into 2 halves baseed on idx, then apply BS to both

        l1 = 0
        h1 = idx - 1
        while(l1 <= h1):
            mid1 = (l1 + h1)//2
            if nums[mid1] == target:
                return mid1
            elif nums[mid1] > target:
                h1 = mid1 - 1
            else:
                l1 = mid1 + 1
        
        l2 = idx
        h2 = n - 1
        while l2 <= h2:
            mid2 = (l2 + h2)//2
            if nums[mid2] == target:
                return mid2
            elif nums[mid2] > target:
                h2 = mid2 - 1
            else:
                l2 = mid2 + 1
        return -1