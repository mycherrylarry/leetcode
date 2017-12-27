using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions.DP
{
    class UniquePathsII
    {
        public int UniquePathsWithObstacles(int[,] grid)
        {
            int m = grid.GetLength(0);
            int n = grid.GetLength(1);
            if (m == 0 || n == 0) return 0;
            int[,] dp = new int[m, n];
            dp[0, 0] = grid[0, 0] == 0 ? 1 : 0;
            for (int i = 1; i < m; i++)
            {
                dp[i, 0] = grid[i, 0] == 0 ? dp[i - 1, 0] : 0;
            }

            for (int j = 1; j < n; j++)
            {
                dp[0, j] = grid[0, j] == 0 ? dp[0, j - 1] : 0;
            }

            for (int i = 1; i < m; i++)
            {
                for (int j = 1; j < n; j++)
                {
                    dp[i, j] = grid[i, j] == 0 ? dp[i - 1, j] + dp[i, j - 1] : 0;
                }
            }

            return dp[m - 1, n - 1];
        }
    }
}
