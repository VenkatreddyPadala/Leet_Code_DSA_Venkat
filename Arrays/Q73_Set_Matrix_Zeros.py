class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        for i in zero_rows:
            for j in range(n):
                matrix[i][j] = 0
        for j in zero_cols:
            for i in range(m):
                matrix[i][j] = 0
        return matrix
    