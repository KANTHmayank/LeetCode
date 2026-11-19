class Solution:
    
    def lessThanOrEqualI(self, matrix: list[list[int]], i: int) -> int:
        n = len(matrix)
        count = 0
        row = n - 1
        col = 0
        while row >= 0 and col < n:
            if matrix[row][col] <= i:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count

    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        res = -1
        while low <= high:
            guess = (low + high) // 2
            # row = guess // n
            # col = guess % n

            if self.lessThanOrEqualI(matrix, guess) < k:
                low = guess + 1
            else:
                res = guess
                high = guess - 1
        return res