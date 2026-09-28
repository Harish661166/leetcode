class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return [
            [matrix[i][j] for i in range(len(matrix))]
            for j in range(len(matrix[0]))
        ]