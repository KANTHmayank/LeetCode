class Solution:
    def lessThanOrEqualI(self, m: int, n: int, i: int) -> int:
        # m = len(matrix)
        # m = len(matrix[0])
        count = 0
        row = m 
        col = 1
        while row > 0 and col <= n:
            if row * col <= i:
                count += row 
                col += 1
            else:
                row -= 1
        return count
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # l = len(matrix)
        # m = len(matrix[0])
        low = 1
        high = m * n
        res = -1
        while low <= high:
            guess = (low + high) // 2
            # row = guess // n
            # col = guess % n

            if self.lessThanOrEqualI(m,n, guess) < k:
                low = guess + 1
            else:
                res = guess
                high = guess - 1
        return res