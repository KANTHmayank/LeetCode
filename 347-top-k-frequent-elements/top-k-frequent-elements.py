class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ans = []
        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0) + 1

        sorted_freq = dict(sorted(freq.items(), key = lambda x : x[1], reverse = True))

        for key in sorted_freq:
            
            ans.append(key)
            if len(ans) == k:
                break

        return ans
