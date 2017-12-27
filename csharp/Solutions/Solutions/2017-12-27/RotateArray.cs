using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_27
{
    class RotateArray
    {
        public void Rotate(int[] nums, int k)
        {
            int n = nums.Length;
            if (n == 0 || n == 1) return;
            k = k % n;
            if (k == 0) return;

            Reverse(nums, 0, n - k - 1);
            Reverse(nums, n - k, n - 1);
            Reverse(nums, 0, n - 1);
        }

        private void Reverse(int[] nums, int i, int j)
        {
            while (i < j)
            {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++; j--;
            }
        }
    }
}
