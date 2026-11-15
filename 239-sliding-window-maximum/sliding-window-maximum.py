from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        dq = deque()
        n = len(nums)
        for i in range(n):
            # Step 1: Window size check
            while(dq and dq[0] <= i- k):
                dq.popleft()

            # sTep 2: smaller element check
            while(dq and nums[i] >= nums[dq[-1]]):
                dq.pop()

            #Step 3: insert ele in deque
            dq.append(i)

            #styep-4 window complete, add max to result

            if i >= k-1:
                result.append(nums[dq[0]])
        return result
            