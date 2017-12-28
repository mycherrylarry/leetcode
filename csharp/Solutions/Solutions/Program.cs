using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Solutions._2017_12_28;

namespace Solutions
{
    class Program
    {
        static void Main(string[] args)
        {
            ReplcateWords word = new ReplcateWords();
            List<string> list = new List<string>();
            list.Add("cat");
            list.Add("bat");
            list.Add("rat");

            Console.WriteLine(word.ReplaceWords(list, "the cattle was rattled by the battery"));
        }

        static void ChangeNumber(ref int n)
        {
            n = n + 1;
        }
    }
}
