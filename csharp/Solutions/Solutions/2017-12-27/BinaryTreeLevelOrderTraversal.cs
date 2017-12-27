using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_27
{
    class BinaryTreeLevelOrderTraversal
    {
        public IList<IList<int>> LevelOrder(TreeNode root)
        {
            IList<IList<int>> result = new List<IList<int>>();
            if (root == null) return result;

            Queue<TreeNode> queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            while (queue.Count != 0)
            {
                List<int> temp = new List<int>();
                int count = queue.Count();
                for (int i = 0; i < count; i++)
                {
                    TreeNode top = queue.Dequeue();
                    temp.Add(top.val);
                    if (top.left != null) queue.Enqueue(top.left);
                    if (top.right != null) queue.Enqueue(top.right);
                }

                result.Add(temp);
            }

            return result;
        }
    }
}
