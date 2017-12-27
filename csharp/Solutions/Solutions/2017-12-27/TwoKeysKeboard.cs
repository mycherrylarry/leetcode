using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_27
{
    class TwoKeysKeboard
    {
        public int MinSteps(int n)
        {
            if (n == 0 || n == 1) return 0;
            int[] dp = new int[n + 1];

            for (int i = 2; i <= n; i++)
            {
                dp[i] = int.MaxValue;

                for (int j = 1; j <= i / 2; j++)
                {
                    if (i % j == 0)
                    {
                        dp[i] = Math.Min(dp[i], dp[j] + i / j);
                    }
                }
            }

            return dp[n];
        }
    }
}
