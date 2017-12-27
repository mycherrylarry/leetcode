using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_27
{
    class FindLargestValueInEachTreeRow
    {
        public IList<int> LargestValues(TreeNode root)
        {
            List<int> result = new List<int>();
            if (root == null) return result;
            Queue<TreeNode> queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            while (queue.Count != 0)
            {
                int n = queue.Count;
                int max = int.MinValue;
                for (int i = 0; i < n; i++)
                {
                    TreeNode top = queue.Dequeue();
                    max = Math.Max(max, top.val);
                    if (top.left != null) queue.Enqueue(top.left);
                    if (top.right != null) queue.Enqueue(top.right);
                }

                result.Add(max);
            }

            return result;
        }
    }
}
