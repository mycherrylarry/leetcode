using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_27
{
    class LexicographicalNumber
    {
        public IList<int> LexicalOrder(int n)
        {
            List<int> result = new List<int>();
            Solve(1, n, result);
            return result;
        }

        private void Solve(int m, int n, List<int> result)
        {
            result.Add(m);
            if (m * 10 <= n) Solve(m * 10, n, result);
            if (m < n && m % 10 < 9) Solve(m + 1, n, result);
        }
    }
}
