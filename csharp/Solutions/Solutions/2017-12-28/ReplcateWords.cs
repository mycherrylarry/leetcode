using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Solutions._2017_12_28
{
    /// <summary>
    /// Wrong answer
    /// </summary>
    class ReplcateWords
    {
        public string ReplaceWords(IList<string> dict, string sentence)
        {
            int n = sentence.Length;
            if (n == 0 || n == 1) return sentence;

            StringBuilder sb = new StringBuilder();
            int i = 0;
            while (sentence[i] == ' ' && i < n)
            {
                sb.Append(' ');
                i++;
            }

            if (i == n) return sb.ToString();

            Trie trie = new Trie();
            foreach (var item in dict)
            {
                trie.Add(item);
            }

            int j = i + 1;
            while (j < n)
            {
                if (sentence[j] == ' ')
                {
                    if (sentence[i] != ' ')
                    {
                        string subword = sentence.Substring(i, j - i);
                        sb.Append(trie.GetRoot(subword));
                    }
                    else
                    {
                        i = j;
                    }

                    sb.Append(' ');
                }

                j++;
            }

            if (sentence[i] != ' ')
            {
                string subword = sentence.Substring(i, j - i);
                sb.Append(trie.GetRoot(subword));
            }

            return sb.ToString();
        }

        public class TrieNode
        {
            public char Character { get; set; }
            public TrieNode[] Children { get; set; }
            public bool IsWord { get; set; }

            public TrieNode(char c, bool isWord = false)
            {
                this.Character = c;
                this.Children = new TrieNode[26];
                this.IsWord = isWord;
            }
        }

        public class Trie
        {
            private TrieNode root;
            public Trie()
            {
                root = new TrieNode('a');
            }

            public void Add(string str)
            {
                TrieNode p = root;
                for (int i = 0; i < str.Length; i++)
                {
                    int index = str[i] - 'a';
                    if (p.Children[index] == null)
                    {
                        p.Children[index] = new TrieNode(str[i]);
                    }

                    if (i == str.Length - 1)
                    {
                        p.Children[index].IsWord = true;
                    }

                    p = p.Children[index];
                }
            }

            public string GetRoot(string str)
            {
                TrieNode p = root;
                for (int i = 0; i < str.Length; i++)
                {
                    TrieNode child = p.Children[str[i] - 'a'];
                    if (child == null)
                    {
                        return str;
                    }

                    if (child.IsWord)
                    {
                        return str.Substring(0, i + 1);
                    }

                    p = child;
                }

                return str;
            }
        }
    }
}
