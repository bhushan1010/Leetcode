class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        flat = [0] * (m*n)
        for i in range(m):
            for j in range(n):
                idx = (i*n+j+k) % (m*n)
                flat[idx] = grid[i][j]
        return [flat[i*n: (i +1) *n] for i in range(m)]