class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        #narrow down to which row
        while top < bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                if matrix[mid+1][0] <= target:
                    top = mid + 1
                else:
                    top = mid
                    break
            else:
                bottom = mid - 1

        left = 0
        right = len(matrix[top]) - 1
        row = matrix[top]
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False