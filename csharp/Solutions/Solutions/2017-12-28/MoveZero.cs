using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_28
{
    class MoveZero
    {
        public void MoveZeroes(int[] nums)
        {
            int n = nums.Length;
            if (n == 0 || n == 1) return;
            int i = 0, j = 0;
            while (j < n)
            {
                if (nums[j] != 0)
                {
                    if (i != j)
                    {
                        nums[i] = nums[j];
                    }

                    i++;
                }

                j++;
            }

            while (i < n)
            {
                nums[i++] = 0;
            }

        }
    }
}
