using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_28
{
    class CountAndSay
    {
        public string CountAndSayM(int n)
        {
            if (n < 1) return null;
            string result = "1";
            for (int i = 1; i < n; i++)
            {
                result = GetNext(result);
            }

            return result;
        }

        private string GetNext(string input)
        {
            StringBuilder sb = new StringBuilder();
            int count = 1, i = 1;
            while (i < input.Length)
            {
                if (input[i] == input[i - 1])
                {
                    count++;
                }
                else
                {
                    sb.Append(count);
                    sb.Append(input[i - 1]);
                    count = 1;
                }

                i++;
            }

            sb.Append(count);
            sb.Append(input[i - 1]);

            return sb.ToString();
        }
    }
}
