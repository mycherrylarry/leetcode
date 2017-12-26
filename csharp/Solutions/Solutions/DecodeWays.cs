using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions
{
    class DecodeWays
    {
        public int NumDecodings(string s)
        {
            if (s.Length == 0) return 0;
            int[] dp = new int[s.Length + 1];
            dp[0] = 1;
            dp[1] = s[0] == '0' ? 0 : 1;
            for (int i = 2; i <= s.Length; i++)
            {
                if (s[i - 1] == '0')
                {
                    if (s[i - 2] == '1' || s[i - 2] == '2')
                    {
                        dp[i] = dp[i - 2];
                    }
                    else
                    {
                        dp[i] = 0;
                    }
                }
                else
                {
                    int sum = (s[i - 2] - '0') * 10 + s[i - 1] - '0';
                    if (sum >= 11 && sum <= 26)
                    {
                        dp[i] = dp[i - 1] + dp[i - 2];
                    }
                    else
                    {
                        dp[i] = dp[i - 1];
                    }
                }
            }

            return dp[s.Length];
        }
    }
}
