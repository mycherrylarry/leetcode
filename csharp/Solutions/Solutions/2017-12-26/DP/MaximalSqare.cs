using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions.DP
{
    class MaximalSqare
    {
        public int MaximalSquare(char[,] matrix)
        {
            int result = 0;
            int m = matrix.GetLength(0);
            int n = matrix.GetLength(1);
            if (m == 0 || n == 0) return result;
            int[,] dp = new int[m, n];
            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (matrix[i, j] == '1')
                    {
                        if (i == 0 || j == 0)
                            dp[i, j] = 1;
                        else
                        {
                            int col = 0;
                            int row = 0;
                            for (int k = 0; k <= dp[i - 1, j - 1]; k++)
                            {
                                if (matrix[i - k, j] == '1') row++;
                                else break;
                            }
                            for (int k = 0; k <= dp[i - 1, j - 1]; k++)
                            {
                                if (matrix[i, j - k] == '1') col++;
                                else break;
                            }

                            dp[i, j] = Math.Min(col, row);
                        }

                        result = Math.Max(dp[i, j], result);
                    }
                }
            }

            return result * result;
        }
    }
}
