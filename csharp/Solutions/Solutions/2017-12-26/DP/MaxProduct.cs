using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions.DP
{
    class MaxProduct
    {
        // Exceed time limit.
        public int AxProduct(int[] nums)
        {
            if (nums.Length == 0) return 0;
            int[] maxDp = new int[nums.Length];
            int[] minDp = new int[nums.Length];
            maxDp[0] = nums[0]; minDp[0] = nums[0];
            int result = nums[0];
            for (int i = 1; i < nums.Length; i++)
            {
                int a = maxDp[i - 1] * nums[i];
                int b = minDp[i - 1] * nums[i];
                maxDp[i] = Math.Max(a, Math.Max(b, nums[i]));
                minDp[i] = Math.Min(a, Math.Min(b, nums[i]));
                result = Math.Max(maxDp[i], result);
            }

            return result;
        }
    }
}
