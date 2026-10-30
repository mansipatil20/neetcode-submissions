class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, rows*cols -1
        while start <= end:
            mid = (start+end) //2
            row, col = divmod(mid, cols)
            val = matrix[row][col]
            if val == target:
                return True
            if val < target:
                start = mid +1
            else:
                end = mid -1

        return False