package solution.pow;

/**
 * Problem: Implement pow(x, n).
 * Method:
 * Solution:
 * Time Complexity:
 * Space Complexity:
 * Result: ERROR
 * Note: consider about edge case.
 */
public class Solution {
    /**
     * Solve the problem when n is positive.
     *
     * @param x
     * @param n
     * @return
     */
    public double solve(double x, int n) {
        if (n == 0) return 1.0;
        if (n == 1) return x;
        double remainder = solve(x, n % 2);
        double half = solve(x, n / 2);
        return half * half * remainder;
    }

    public double pow(double x, int n) {
        if(n == Integer.MIN_VALUE) n += 1;
        return n > 0 ? solve(x, n) : 1.0 / solve(x, -n);
    }
}

class TestCase {

    public static void main(String[] args) {
        Solution s = new Solution();
        double test = s.pow(2.00000, -2147483648);
        System.out.println(test);
        int x = -2147483648;
        System.out.println(-x);
        System.out.println(Math.pow(2.000, x));
    }
}
