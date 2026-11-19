class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # l = 0
        # h = m - 1
        # res = -1
        # while l <= h: # Binary search on every row's first element
        #     guess = (l + h) // 2
        #     if matrix[guess][0] <= target:
        #         res = guess
        #         l = guess + 1
        #     else:
        #         h = guess - 1

        # l = 0
        # h = n - 1
        # while l <= h: # Bianry search on Resultant row
        #     guess = (l + h) // 2
        #     if matrix[res][guess] == target:
        #         return True
        #     elif matrix[res][guess] < target:
        #         l = guess + 1
        #     else:
        #         h = guess - 1
        # return False


        l = 0
        h = (m)*(n) - 1

        while l <= h:
            guess = (l + h)//2

            row = guess // n
            col = guess % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = guess + 1
            else:
                h = guess - 1
        return False