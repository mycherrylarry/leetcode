using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_27
{
    class NumberOfIslands
    {
        public int NumIslands(char[,] grid)
        {
            int m = grid.GetLength(0);
            int n = grid.GetLength(1);
            int result = 0;
            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (grid[i, j] == '1')
                    {
                        result++;
                        Dfs(grid, i, j, m, n);
                    }
                }
            }

            return result;
        }

        private void Dfs(char[,] grid, int i, int j, int m, int n)
        {
            if (i < 0 || j < 0 || i >= m || j >= n || grid[i, j] == '0') return;
            grid[i, j] = '0';
            Dfs(grid, i - 1, j, m, n);
            Dfs(grid, i + 1, j, m, n);
            Dfs(grid, i, j - 1, m, n);
            Dfs(grid, i, j + 1, m, n);
        }
    }
}
