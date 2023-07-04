class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        # Track rows and columns to be set to zero
        zero_rows = set()
        zero_cols = set()

        # Find the rows and columns containing zeros
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        # Set rows and columns to zero
        for row in zero_rows:
            for col in range(n):
                matrix[row][col] = 0

        for col in zero_cols:
            for row in range(m):
                matrix[row][col] = 0    
