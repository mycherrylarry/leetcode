package solution.valid_parentheses;

import java.util.Stack;

/**
 * Problem:
 * Method:
 * Solution:
 * Time Complexity:
 * Space Complexity:
 * Result: AC
 * Note:
 */
public class Solution {
    public boolean isValid(String s) {
        if (s.length() == 0) return true;
        Stack<Character> stack = new Stack<Character>();
        int i = 0;
        while (i < s.length()) {
            char c = s.charAt(i);
            switch (c) {
                case '(':
                case '[':
                case '{':
                    stack.push(c);
                    break;
                case ')':
                    if (stack.isEmpty() || stack.peek() != '(')
                        return false;
                    stack.pop();
                    break;
                case ']':
                    if (stack.isEmpty() || stack.peek() != '[')
                        return false;
                    stack.pop();
                    break;
                case '}':
                    if (stack.isEmpty() || stack.peek() != '{')
                        return false;
                    stack.pop();
            }
            ++i;
        }
        if (!stack.isEmpty())
            return false;
        return true;
    }
}

class TestCase {

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.isValid("[[]}"));
        System.out.println(s.isValid("[[]]"));
        System.out.println(s.isValid("[()]"));
    }
}
