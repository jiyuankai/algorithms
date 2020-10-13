# 542. 01 Matrix

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

class Solution:

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        max_r = len(matrix) - 1
        max_c = len(matrix[0]) - 1
        queue = []
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                if matrix[r][c] == 0:
                    queue.append((r, c))
                else:
                    matrix[r][c] = -1

        while queue:
            r, c = queue.pop(0)
            for direction in directions:
                x, y = direction
                new_r = r + x
                new_c = c + y
                if new_r >= 0 and new_r <= max_r and new_c >= 0 and new_c <= max_c and matrix[new_r][new_c] == -1:
                    matrix[new_r][new_c] = matrix[r][c] + 1
                    queue.append((new_r, new_c))
        return matrix