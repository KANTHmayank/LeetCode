class Solution:
    def tripsCompleted(self, time: list[int], totalTrips: int, x: int) -> bool:
        total = 0
        for i in range(len(time)):
            total += x // time[i]
        return total >= totalTrips
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        l = (totalTrips*min(time)) // len(time)
        h = max(time) * totalTrips
        ans = h 
        while l <= h:
            mid = (l + h) // 2
            if(self.tripsCompleted(time, totalTrips, mid)):
                ans =mid
                h = mid - 1
            else:
                l = mid + 1

        return ans