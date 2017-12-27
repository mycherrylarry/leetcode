using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions
{
    class ReverseWordsInAString
    {
        public static void RunTests()
        {
            ReverseWordsInAString s = new ReverseWordsInAString();
            Console.WriteLine(s.ReverseWords("a blue  sky  "));
        }

        public string ReverseWords(string s)
        {
            if (s.Length == 0 || s.Length == 1) return s;
            List<char> str = new List<char>();
            List<char> result = new List<char>();
            for (int i = 0; i < s.Length; i++)
            {
                if (s[i] == ' ')
                {
                    result.AddRange(ReverseString(str));
                    result.Add(s[i]);
                    str.Clear();
                }
                else
                {
                    str.Add(s[i]);
                    Console.WriteLine(string.Format(" ", str));
                }
            }

            result.AddRange(ReverseString(str));

            return string.Format("", ReverseString(result));
        }

        public List<char> ReverseString(List<char> str)
        {
            int i = 0, j = str.Count - 1;
            while (i < j)
            {
                char temp = str[i];
                str[i] = str[j];
                str[j] = temp;
                i++; j--;
            }

            return str;
        }
    }
}
