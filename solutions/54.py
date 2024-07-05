# Title: Spiral Matrix
# Category: Matrix
# Difficulty: Medium 

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []

        result = [] 
        num_rows, num_cols = len(matrix), len(matrix[0])
        left_bound, right_bound = 0, num_cols - 1
        top_bound, lower_bound = 0, num_rows - 1

        while left_bound <= right_bound and top_bound <= lower_bound:
            # Left To Right 
            for col in range(left_bound, right_bound + 1):
                result.append(matrix[top_bound][col])
            top_bound += 1 

            # Top To Bottom (last column) 
            for row in range(top_bound, lower_bound + 1): 
                result.append(matrix[row][right_bound])
            right_bound -= 1

            # Right To Left (last row)
            if top_bound <= lower_bound: 
                for col in range(right_bound, left_bound - 1, -1): 
                    result.append(matrix[lower_bound][col])
                lower_bound -= 1

            # Bottom to Top (first column) 
            if left_bound <= right_bound:
                for row in range(lower_bound, top_bound - 1, -1): 
                    result.append(matrix[row][left_bound])
                left_bound += 1 
        return result