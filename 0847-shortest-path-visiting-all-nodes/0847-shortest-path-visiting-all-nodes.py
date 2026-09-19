from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        n = len(graph); full = (1<<n)-1
        q = deque(); vis = set()
        for i in range(n):
            q.append((i,1<<i)); vis.add((i,1<<i))
        steps = 0
        while q:
            for _ in range(len(q)):
                nd,mask = q.popleft()
                if mask==full: return steps
                for nb in graph[nd]:
                    nm = mask|(1<<nb)
                    if (nb,nm) not in vis: vis.add((nb,nm)); q.append((nb,nm))
            steps += 1
        return -1