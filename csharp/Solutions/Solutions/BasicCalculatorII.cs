using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions
{
    class BasicCalculatorII
    {
        public int Calculate(string s)
        {
            int num = 0;
            int result = 0;
            int i = 0;
            char preSign = '+';
            Stack<int> stack = new Stack<int>();

            for (i = 0; i < s.Length; i++)
            {
                if (s[i] >= '0' && s[i] <= '9')
                {
                    num = num * 10 + s[i] - '0';
                }
                else if (s[i] == ' ')
                {
                    continue;
                }
                else
                {
                    CheckSign(stack, num, preSign);
                    preSign = s[i];
                    num = 0;
                }
            }

            CheckSign(stack, num, preSign);

            while (stack.Count != 0)
            {
                result += stack.Pop();
            }

            return result;
        }

        private void CheckSign(Stack<int> stack, int num, char preSign)
        {
            if (preSign == '+')
            {
                stack.Push(num);
            }
            else if (preSign == '-')
            {
                stack.Push(-num);
            }
            else if (preSign == '*')
            {
                int top = stack.Pop();
                stack.Push(top * num);
            }
            else if (preSign == '/')
            {
                int top = stack.Pop();
                stack.Push(top / num);
            }
        }

    }
}
