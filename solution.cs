```C#
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<string> strings = new List<string> { "flower", "flow", "flight" };
        Console.WriteLine(LongestCommonPrefix(strings));
    }

    static string LongestCommonPrefix(List<string> strs)
    {
        if (strs.Count == 0) return "";
        string prefix = strs[0];
        for (int i = 1; i < strs.Count; i++)
        {
            while (strs[i].IndexOf(prefix) != 0)
            {
                prefix = prefix.Substring(0, prefix.Length - 1);
                if (string.IsNullOrEmpty(prefix)) return "";
            }
        }
        return prefix;
    }
}
```