package solution.UniqueBinaryTreesII;

import util.TreeNode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
    public List<TreeNode> generate(int[] range) {
        List<TreeNode> result = new ArrayList<TreeNode>();
        if (range.length == 0) {
            result.add(null);
            return result;
        }
        if (range.length == 1) {
            result.add(new TreeNode(range[0]));
            return result;
        }
        for (int i = 0; i < range.length; ++i) {
            List<TreeNode> left = this.generate(Arrays.copyOfRange(range, 0, i));
            List<TreeNode> right = this.generate(Arrays.copyOfRange(range, i + 1, range.length));
            for (TreeNode item_l : left) {
                for (TreeNode item_r : right) {
                    TreeNode root = new TreeNode(range[i]);
                    root.left = item_l;
                    root.right = item_r;
                    result.add(root);
                }
            }
        }
        return result;
    }

    public List<TreeNode> generateTrees(int n) {
        int[] range = new int[n];
        for (int i = 1; i <= n; ++i) {
            range[i - 1] = i;
        }
        return this.generate(range);
    }
}

class TestCase {

    public static void main(String[] args) {
    }
}
