using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_27
{
    class GroupAnagrams
    {
        public IList<IList<string>> GroupAnagramsx(string[] strs)
        {
            IList<IList<string>> result = new List<IList<string>>();
            Dictionary<string, List<string>> map = new Dictionary<string, List<string>>();

            for (int i = 0; i < strs.Length; i++)
            {
                string s = string.Concat(strs[i].OrderBy(c => c));
                if (!map.ContainsKey(s))
                {
                    map[s] = new List<string>();
                }

                map[s].Add(strs[i]);
            }

            foreach (var items in map)
            {
                result.Add(items.Value);
            }

            return result;
        }
    }
}
