using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_28
{
    class FindMaxConsecutiveOnes
    {
        public int fFindMaxConsecutiveOnes(int[] nums)
        {
            if (nums.Length == 0) return 0;
            int result = 0;

            int left = -1, right = 0;
            while (right < nums.Length)
            {
                if (nums[right] == 1)
                {
                    result = Math.Max(result, right - left);
                }
                else
                {
                    left = right;
                }

                right++;
            }


            return result;
        }
    }
}
