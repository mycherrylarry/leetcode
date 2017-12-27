using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_27
{
    class PathSumIII
    {
        /// <summary>
        /// Find path sum from root to leaf, but not be the one.
        /// </summary>
        /// <param name="root"></param>
        /// <param name="sum"></param>
        /// <returns></returns>
        public int PathSum(TreeNode root, int sum)
        {
            if (root == null) return 0;
            int count = 0;
            Dfs(root, sum, ref count);

            return count + PathSum(root.left, sum) + PathSum(root.right, sum);
        }

        /// <summary>
        /// Find dfs
        /// </summary>
        /// <param name="root"></param>
        /// <param name="sum"></param>
        /// <param name="count"></param>
        private void Dfs(TreeNode root, int sum, ref int count)
        {
            if (root == null) return;
            if (root.val == sum) count++;
            Dfs(root.left, sum - root.val, ref count);
            Dfs(root.right, sum - root.val, ref count);
        }
    }
}
