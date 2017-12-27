using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_27
{
    class AverageOfLevelsInBinaryTree
    {
        public IList<double> AverageOfLevels(TreeNode root)
        {
            IList<double> result = new List<double>();
            if (root == null) return result;

            Queue<TreeNode> queue = new Queue<TreeNode>();
            queue.Enqueue(root);

            while (queue.Count != 0)
            {
                int count = queue.Count;
                double sum = 0;
                for (int i = 0; i < count; i++)
                {
                    TreeNode top = queue.Dequeue();
                    sum += top.val;
                    if (top.left != null) queue.Enqueue(top.left);
                    if (top.right != null) queue.Enqueue(top.right);
                }

                result.Add(sum / count);
            }

            return result;
        }
    }
}
