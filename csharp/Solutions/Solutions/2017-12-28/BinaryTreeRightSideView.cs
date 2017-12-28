using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_28
{
    class BinaryTreeRightSideView
    {
        public IList<int> RightSideView(TreeNode root)
        {
            IList<int> result = new List<int>();
            if (root == null) return result;

            Queue<TreeNode> queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            while (queue.Count != 0)
            {
                int count = queue.Count;
                for (int i = 0; i < count; i++)
                {
                    TreeNode peek = queue.Dequeue();
                    if (i == count - 1) result.Add(peek.val);
                    if (peek.left != null) queue.Enqueue(peek.left);
                    if (peek.right != null) queue.Enqueue(peek.right);
                }
            }

            return result;
        }
    }
}
