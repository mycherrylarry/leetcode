using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions
{
    class FizzBuzzQ
    {
        public IList<string> FizzBuzz(int n)
        {
            int[] flags = new int[n];
            int i = 2;
            while (i < n)
            {
                flags[i]++;
                i += 3;
            }

            i = 4;
            while (i < n)
            {
                flags[i]++;
                i += 5;
            }
            List<string> result = new List<string>();
            for (i = 0; i < n; i++)
            {
                if (flags[i] == 1)
                {
                    result.Add((i + 1) % 3 == 0 ? "Fizz" : "Buzz");
                }
                else if (flags[i] == 2)
                {
                    result.Add("FizzBuzz");
                }
                else
                    result.Add((i + 1).ToString());
            }

            return result;
        }
    }
}
