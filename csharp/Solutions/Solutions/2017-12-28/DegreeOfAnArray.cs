using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_28
{
    class DegreeOfAnArray
    {
        public int FindShortestSubArray(int[] nums)
        {
            int n = nums.Length;
            if (n == 0 || n == 1) return n;

            Dictionary<int, int> map = new Dictionary<int, int>();
            int max = 0;
            for (int i = 0; i < n; i++)
            {
                if (!map.ContainsKey(nums[i]))
                {
                    map[nums[i]] = 0;
                }

                map[nums[i]]++;
                max = Math.Max(map[nums[i]], max);
            }
            List<int> bigItems = new List<int>();
            foreach (var pair in map)
            {
                if (pair.Value == max)
                {
                    bigItems.Add(pair.Key);
                }
            }

            int result = n;

            foreach (int item in bigItems)
            {
                int left = 0, right = n - 1;
                while (nums[left] != item) left++;
                while (nums[right] != item) right--;

                result = Math.Min(result, right - left + 1);
            }

            return result;
        }
    }
}
