using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_27
{
    class TwoSumII
    {
        public int[] TwoSum(int[] numbers, int target)
        {
            int left = 0, right = numbers.Length - 1;
            while (left < right)
            {
                int sum = numbers[left] + numbers[right];
                if (sum == target)
                {
                    break;
                }
                else if (sum > target)
                {
                    right--;
                }
                else
                {
                    left++;
                }
            }

            return new int[] { left + 1, right + 1 };
        }
    }
}
