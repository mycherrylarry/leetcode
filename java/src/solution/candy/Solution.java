package solution.candy;

/**
 * Problem:
 *  You are giving candies to these children subjected to the following requirements:
 *      1. Each child must have at least one candy.
 *      2. Children with a higher rating get more candies than their neighbors.
 * Method: Two way traverse
 * Solution:
 * Time Complexity: O(N)
 * Space Complexity:
 * Result: AC
 * Note:
 */

public class Solution {
    public int candy(int[] ratings) {
        if(ratings.length == 0) return 0;
        if(ratings.length == 1) return 1;
        int[] route = new int[ratings.length];
        route[0] = 1;
        // traverse from left to right
        for(int i = 1; i< ratings.length; i++) {
            if(ratings[i] > ratings[i-1]) {
                route[i] = route[i-1] + 1;
            } else {
                route[i] = 1;
            }
        }
        // traverse from right to left
        for(int i = ratings.length-2; i>= 0; i--) {
            if(ratings[i] > ratings[i+1]) {
                route[i] = Math.max(route[i+1]+1, route[i]);
            }
        }
        int result = 0;
        for(int item: route) {
            result += item;
        }
        return result;
    }
}

class TestCase {

    public static void main(String[] args) {
        Solution s = new Solution();
        s.candy(new int[]{4,1,3,3,3,2,7,2,1,3});
        System.out.println("hello");
    }
}
