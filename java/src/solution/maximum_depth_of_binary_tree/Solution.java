package solution.maximum_depth_of_binary_tree;

import util.Tree;
import util.TreeNode;

import java.lang.Math;

/**
 * Returns the maximum depth of a tree
 *
 */
public class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null) return 0;
        return Math.max(maxDepth(root.left), maxDepth(root.right))+1;
    }
}

class TestCase {

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println("hello");
        TreeNode root = Tree.create(new int[]{1, 2});
        Tree.prettyPrint(root);
        System.out.println(s.maxDepth(root));
    }
}
