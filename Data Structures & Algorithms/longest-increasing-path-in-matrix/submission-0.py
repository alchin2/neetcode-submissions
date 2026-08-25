class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        directions = [(-1,0), (0,-1), (1,0), (0,1)]

        def dfs(x, y):
            if dp[x][y]!= -1:
                return dp[x][y]

            max_len = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    max_len = max(max_len, 1 + dfs(nx, ny))
            
            dp[x][y] = max_len
            return dp[x][y]

        for i in range(m):
            for j in range(n):
                dfs(i, j)

        print(dp)
        return max(max(row) for row in dp)
            
                
