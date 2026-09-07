class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0]*m for _ in range(n)]
        def bfs(row,col):
            area = 1
            q = [[row,col]]
            dx = [-1,0,1,0] #change in row [top,right,down,left]
            dy = [0,1,0,-1] #change in column [top,right,down,left]
            while q:
                f = q.pop(0)
                r = f[0]
                c = f[1]
                for k in range(4):
                    cr = r+dx[k]
                    cc = c+dy[k]
                    if cr >= 0 and cr < n and cc >= 0 and cc < m and visited[cr][cc] == 0 and grid[cr][cc] == 1:
                        visited[cr][cc] = 1
                        q.append([cr,cc])
                        area += 1
            return area            
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    visited[i][j] = 1
                    res = max(res,bfs(i,j))                 
        return res            