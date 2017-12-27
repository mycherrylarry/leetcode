using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 1;
            ChangeNumber(ref n);

            Console.WriteLine(n);
        }

        static void ChangeNumber(ref int n)
        {
            n = n + 1;
        }
    }
}
