package solution.best_time_to_buy_and_sell_stock;

/**
 * Problem:
 * Method:
 * Solution:
 * Time Complexity:
 * Space Complexity:
 * Result:
 * Note:
 */
public class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length == 0 || prices.length == 1)
            return 0;
        int mi = prices[0];
        int result = 0;
        for(int i = 1; i < prices.length; ++i) {
            if(prices[i] < mi)
                mi = prices[i];
            else
                result = Math.max(prices[i] - mi, result);
        }
        return result;
    }
}

class TestCase {

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println("hello");
    }
}
