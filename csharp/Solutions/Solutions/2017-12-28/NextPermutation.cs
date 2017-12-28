using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_28
{
    class NextPermutation
    {
        public void NextPermutation1(int[] nums)
        {
            int n = nums.Length;
            if (n == 0 || n == 1) return;

            int i = n - 2;
            while (i >= 0)
            {
                if (nums[i] < nums[i + 1])
                {
                    break;
                }

                i--;
            }

            if (i < 0)
            {
                Array.Sort(nums);

                return;
            }

            int j = n - 1;
            while (j > i)
            {
                if (nums[j] > nums[i])
                {
                    break;
                }

                j--;
            }

            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;

            Array.Sort(nums, i + 1, n - i - 1);
        }
    }
}
