class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # f = {}
        # low = 0
        # res = -1
        # if len(s) == 0:
        #     return 0
        # if len(s) == 1:
        #     return 1
        # for high in range(len(s)):
        #     f[s[high]] = f.get(s[high], 0) + 1
        #     k = high - low + 1

        #     while len(f) < k:
        #         f[s[low]]= f.get(s[low], 0) - 1
        #         if f[s[low]] == 0:
        #             f.pop(s[low])
        #         low += 1    
        #         k = high - low + 1
        #     length = k
        #     res = max(res, length)
        # return res


        f = {}
        low = 0
        res = 0
        for high in range(len(s)):
            if(s[high] in f):
                low = max(low, f[s[high]] + 1)
            f[s[high]] = high
            res = max(res, high - low + 1)
        return res