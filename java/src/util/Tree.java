package util;

import java.util.ArrayList;

public class Tree {
    public static TreeNode create(int[] li) {
        ArrayList<Integer> intList = new ArrayList<Integer>();
        for (int item : li) {
            intList.add(item);
        }
        return Tree.create(intList);
    }

    public static TreeNode create(ArrayList<Integer> li) {
        if (li.size() == 0) return null;
        int mid = li.size() / 2;
        TreeNode root = new TreeNode(li.get(mid));
        root.left = Tree.create(new ArrayList<Integer>(li.subList(0, mid)));
        root.right = Tree.create(new ArrayList<Integer>(li.subList(mid + 1, li.size())));
        return root;
    }

    public static void prettyPrint(TreeNode root) {
        Tree.prettyPrint(root, 0);
    }

    public static void prettyPrint(TreeNode root, int level) {
        if (root == null) return;
        Tree.prettyPrint(root.right, level + 1);
        for (int i = 0; i < level; i++) {
            System.out.print("==");
        }
        System.out.println(root.val);
        Tree.prettyPrint(root.left, level + 1);
    }

    public static void main(String[] args) {
        TreeNode root = Tree.create(new int[]{1, 2, 3, 4, 5});
        Tree.prettyPrint(root);
    }
}
