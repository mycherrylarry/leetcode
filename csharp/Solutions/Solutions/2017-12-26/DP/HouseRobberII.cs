using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions.DP
{
    class HouseRobberII
    {
        public int Rob(int[] nums)
        {
            if (nums.Length == 0) return 0;
            if (nums.Length == 1) return nums[0];

            return Math.Max(SubRob(nums.ToList().GetRange(1, nums.Length - 1).ToArray()), SubRob(nums.ToList().GetRange(0, nums.Length - 1).ToArray()));
        }

        private int SubRob(int[] nums)
        {
            if (nums.Length == 1) return nums[0];
            int[] dp = new int[nums.Length + 1];
            dp[0] = 0;
            dp[1] = nums[0];
            for (int i = 2; i <= nums.Length; i++)
            {
                dp[i] = Math.Max(dp[i - 1], dp[i - 2] + nums[i - 1]);
            }

            return dp[nums.Length];
        }
    }
}
