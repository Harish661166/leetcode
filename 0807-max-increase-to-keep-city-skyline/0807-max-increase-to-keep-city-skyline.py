class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row=[]
        column=[]
        n=len(grid)
        for i in range(n):
            row.append(max(grid[i]))
            column.append(max(grid[r][i] for r in range(n)))
        count=0
        for i in range(n):
            for j in range(n):
                count+=(min(row[i],column[j])-grid[i][j])
        return count