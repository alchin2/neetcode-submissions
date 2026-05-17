class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0;
        maxRow, maxCol = len(grid), len(grid[0])
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            direction = [[0,1],[1,0],[0,-1],[-1,0]]
            while q:
                r1, c1 = q.popleft()
                for nh, nv in direction:
                    if (r1+nh in range(maxRow) 
                    and c1+nv in range(maxCol) 
                    and (r1+nh,c1+nv) not in visited 
                    and grid[r1][c1]=="1"):
                        q.append((r1+nh,c1+nv))
                        visited.add((r1+nh,c1+nv))
                

        for row in range(maxRow):
            for col in range(maxCol):
                if (grid[row][col]=="1") and (row,col) not in visited:
                    bfs(row,col)
                    islands+=1
        
        return islands