class Solution:
    def digitSum(self, s: str, k: int) -> str:
        s1= list(s)
        # ans = []
        while len(s1) > k:
            ans = []
            j = 0
            count = 0
            for i in range(len(s1)):
                if j >= k:
                    ans.append(str(count))
                    count = 0
                    j = 0
                    

                j += 1
                count += int(s1[i])
            ans.append(str(count))
            s1 = "".join(map(str, ans))
        return "".join(s1)

