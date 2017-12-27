using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions
{
    class BuildTree
    {
        public TreeNode BbuildTree(int[] preorder, int[] inorder)
        {
            if (preorder.Length != inorder.Length || preorder.Length == 0) return null;

            TreeNode root = new TreeNode(preorder[0]);
            int i = 0;
            while (i < inorder.Length)
            {
                if (inorder[i] == preorder[0]) break;
                i++;
            }
            List<int> pre = preorder.ToList();
            List<int> ino = inorder.ToList();
            root.left = BbuildTree(pre.GetRange(1, i).ToArray(), ino.GetRange(0, i).ToArray());
            root.right = BbuildTree(pre.GetRange(i + 1, preorder.Length - i - 1).ToArray(), ino.GetRange(i + 1, preorder.Length - i - 1).ToArray());

            return root;
        }
    }
}
