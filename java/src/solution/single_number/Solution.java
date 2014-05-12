package solution.single_number;

public class Solution {

    public int singleNumber(int[] A) {
        int result = 0;
        for(int item: A) {
            result ^= item;
        }
        return result;
    }

}

class TestCase {

    public static void main(String[] args) {
        Solution s = new Solution();
        int result = s.singleNumber(new int []{1,1,2});
        System.out.println(result);
    }
}
