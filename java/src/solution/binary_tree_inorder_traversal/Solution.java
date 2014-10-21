package solution.binary_tree_inorder_traversal;
import java.util.*;
import util.TreeNode;

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

    private class Pair<K, V> {
        public final K k;
        public final V v;
        public Pair(K k, V v) {
            this.k = k;
            this.v = v;
        }
    }

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if(root == null) return result;
        Stack<Pair<TreeNode, Integer>> stack = new Stack<Pair<TreeNode, Integer>>();
        stack.push(new Pair<TreeNode, Integer>(root, 0));
        while(!stack.isEmpty()) {
            Pair<TreeNode, Integer> pair = stack.pop();
            if(pair.v == 0) {
                stack.push(new Pair<TreeNode, Integer>(pair.k, 1));
                if(pair.k.left != null) {
                    stack.push(new Pair<TreeNode, Integer>(pair.k.left, 0));
                }
            } else {
                result.add(pair.k.val);
                if(pair.k.right != null)
                    stack.push(new Pair<TreeNode, Integer>(pair.k.right, 0));
            }
        }
        return result;
    }
}

class TestCase {

    private class Tuple<K, V, T> {
        final K k;
        final V v;
        final T t;
        Tuple(K k, V v, T t) {
            this.k = k;
            this.v = v;
            this.t = t;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println("hello");
    }
}
