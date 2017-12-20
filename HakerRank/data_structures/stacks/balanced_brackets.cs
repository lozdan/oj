*
author: Daniel Lozano
source: HAckerRank ( https://www.hackerrank.com )
problem name: Data Structures: Stacks: Balanced Brackets
problem url: https://www.hackerrank.com/challenges/balanced-brackets/problem
*/

using System;
using System.Collections.Generic;
using System.Linq;

namespace HackerRank
{
    public class Resolution
    {
        public static void Main()
        {
            int n = int.Parse(Console.ReadLine());
            for (int i = 0; i < n; i++)
            {
                if (BalancedBrackets(Console.ReadLine()))
                    Console.WriteLine("YES");
                else
                    Console.WriteLine("NO");
            }   
        }

        public static bool BalancedBrackets(string brackets)
        {
            Stack<char> stack = new Stack<char>();
            for (int i = 0; i < brackets.Length; i++)
            {
                string check = "([{";
                if (check.Contains(brackets[i]))
                    stack.Push(brackets[i]);
                else if (stack.Count != 0)
                {
                    string lett = brackets[i].ToString();
                    string last_one = stack.Peek().ToString();
                    if (lett == ")" && last_one == "(")
                        stack.Pop();
                    else if (lett == "]" && last_one == "[")
                        stack.Pop();
                    else if (lett == "}" && last_one == "{")
                        stack.Pop();
                }
                else
                    return false;
            }
            if (stack.Count == 0)
                return true;
            return false;
        }
    }
}