using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_27
{
    class FindKClosestElements
    {
        public IList<int> FindClosestElements(int[] arr, int k, int x)
        {
            IList<int> result = new List<int>();
            if (arr.Length == 0) return result;
            if (k > arr.Length) k = arr.Length;

            int insertPosition = BinarySearch(arr, x);

            int left = insertPosition - k < 0 ? 0 : insertPosition - k;
            int right = insertPosition + k >= arr.Length ? arr.Length - 1 : insertPosition + k;

            while ((right - left + 1) > k)
            {
                if (Math.Abs(arr[left] - x) > Math.Abs(arr[right] - x))
                {
                    left++;
                }
                else right--;
            }

            for (int i = left; i <= right; i++)
            {
                result.Add(arr[i]);
            }

            return result;
        }

        private int BinarySearch(int[] array, int target)
        {
            int left = 0, right = array.Length;
            while (left < right)
            {
                int mid = (left + right) / 2;
                if (array[mid] < target)
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid;
                }
            }

            return left;
        }
    }
}
