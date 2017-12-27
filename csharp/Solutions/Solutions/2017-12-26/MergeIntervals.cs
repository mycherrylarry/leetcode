using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions
{
    class MergeIntervals
    {
        public class Interval
        {
            public int start { get; set; }
            public int end { get; set; }
            public Interval() { start = 0; end = 0; }
        }

        public IList<Interval> Merge(List<Interval> intervals)
        {
            if (intervals.Count() == 0 || intervals.Count() == 1) return intervals;

            int i = 0;
            while (i < intervals.Count() - 1)
            {
                if (intervals[i + 1].start <= intervals[i].end)
                {
                    intervals[i].end = Math.Max(intervals[i + 1].end, intervals[i].end);
                    intervals.RemoveAt(i + 1);
                }
                else
                {
                    i++;
                }
            }

            return intervals;
        }
    }
}
