using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_28
{
    class ArrayNesting
    {
        public int xArrayNesting(int[] nums)
        {
            int n = nums.Length;
            if (n == 0 || n == 1) return n;
            int result = 0;
            for (int i = 0; i < n; i++)
            {
                if (nums[i] != -1)
                {
                    int j = i;
                    int count = 0;
                    while (nums[j] != -1)
                    {
                        count++;
                        int temp = nums[j];
                        nums[j] = -1;
                        j = temp;
                    }

                    result = Math.Max(result, count);
                }
            }

            return result;
        }
    }
}
