class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        lo, hi = 0, rows - 1

        while lo <= hi:
            mid = lo + (hi - lo)//2

            if matrix[mid][0] > target:
                hi = mid - 1
            elif matrix[mid][-1] < target:
                lo = mid + 1
            else:
                break

        if lo > hi:
            return False

        row = mid

        lo, hi = 0, cols - 1

        while lo <= hi:
            mid = lo + (hi-lo)//2

            if matrix[row][mid] > target:
                hi = mid - 1
            elif matrix[row][mid] < target:
                lo = mid + 1
            else:
                return True

        return False