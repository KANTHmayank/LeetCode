class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        oddSum = 0
        evenSum = 0
        MOD = 10**9 + 7
        totalOddSub = 0
        for i in range(len(arr)):
            if(arr[i] % 2 != 0):
                
                    evenSum, oddSum = oddSum, evenSum + 1
                
                    
                
                
                
            else:
                
                    oddSum, evenSum = oddSum, evenSum + 1
                
                    
            totalOddSub = (totalOddSub + oddSum) % MOD
        return totalOddSub