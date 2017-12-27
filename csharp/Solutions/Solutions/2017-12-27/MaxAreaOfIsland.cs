using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_27
{
    class MaxAreaOfIsland
    {
        public int MaxAreaOfIland(int[,] grid)
        {
            int m = grid.GetLength(0);
            int n = grid.GetLength(1);
            if (m == 0 || n == 0) return 0;
            int result = 0;
            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (grid[i, j] == 1)
                    {
                        int count = 0;
                        Dfs(grid, i, j, m, n, ref count);
                        result = Math.Max(result, count);
                    }
                }
            }

            return result;
        }

        private void Dfs(int[,] grid, int i, int j, int m, int n, ref int count)
        {
            if (i < 0 || j < 0 || i >= m || j >= n || grid[i, j] == 0) return;
            count++;
            grid[i, j] = 0;

            Dfs(grid, i - 1, j, m, n, ref count);
            Dfs(grid, i + 1, j, m, n, ref count);
            Dfs(grid, i, j - 1, m, n, ref count);
            Dfs(grid, i, j + 1, m, n, ref count);
        }
    }
}
