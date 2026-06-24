class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxSize = 0

        def dfs(r,c):
            size = 0
            temp = [(r,c)]
            visited.add((r,c))

            direction = [(0,1),(1,0),(0,-1),(-1,0)]

            while temp:
                i, j = temp.pop()
                size += 1
                for di, dj in direction:
                    ni = i + di
                    nj = j + dj
                    if 0<=ni<rows and 0<=nj<cols and (ni, nj) not in visited and grid[ni][nj]==1:
                        temp.append((ni, nj))
                        visited.add((ni,nj))

            return size
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visited:
                    maxSize=max(dfs(i,j),maxSize)


        return maxSize        