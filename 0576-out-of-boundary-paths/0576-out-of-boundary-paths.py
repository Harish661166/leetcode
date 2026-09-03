class Solution:
    def findPaths(
        self,
        m: int,
        n: int,
        maxMove: int,
        startRow: int,
        startColumn: int
    ) -> int:

        def dfs(x, y, move):
            # Successfully moved outside the grid
            if x < 0 or x >= row:
                return 1
            if y < 0 or y >= col:
                return 1

            # No moves remaining
            if move <= 0:
                return 0

            # Return cached result
            if (x, y, move) in memo:
                return memo[(x, y, move)]

            # Explore all four directions
            count = (
                dfs(x - 1, y, move - 1)
                + dfs(x + 1, y, move - 1)
                + dfs(x, y - 1, move - 1)
                + dfs(x, y + 1, move - 1)
            )

            memo[(x, y, move)] = count
            return count

        row, col = m, n
        memo = {}
        MOD = 10**9 + 7

        return dfs(startRow, startColumn, maxMove) % MOD