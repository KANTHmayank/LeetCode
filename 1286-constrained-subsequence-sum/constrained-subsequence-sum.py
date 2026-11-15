from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        dq = deque()
        for i in range(len(nums)):
            while(dq and dq[0] < i - k):
                dq.popleft()

            if(dq and nums[dq[0]] > 0):
                nums[i] += nums[dq[0]]

            while(dq and nums[i] >= nums[dq[-1]]):
                dq.pop()

            dq.append(i)

        return max(nums)

            