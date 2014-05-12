package solution.same_tree;

import util.TreeNode;

/**
 * Result: AC
 */
public class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null) return false;
        if (q == null) return false;
        if (p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}

class TestCase {

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println("hello");
    }
}
