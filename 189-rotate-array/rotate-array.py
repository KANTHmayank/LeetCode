class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # nums1 = []
        # for x in nums:
        #     nums1.append(x)
        # del nums[:n]

        # k = k % n

        # for i in nums1[n-k:]:
        #     nums.append(i)
        # for i in nums1[:n-k]:
        #     nums.append(i)
        k = k % n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        
        