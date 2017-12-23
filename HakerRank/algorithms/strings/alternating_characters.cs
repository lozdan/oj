/*
author: Daniel Lozano
source: HackerRank(https://www.hackerrank.com )
problem name: Algorithms > Strings > Alternating Characters
problem url: https://www.hackerrank.com/challenges/alternating-characters/problem
*/

using System;

namespace HackerRank
{
    class Program
    {
        static void Main()
        {
            int n = int.Parse(Console.ReadLine());
                        
            for (int i = 0; i < n; i++)
            {
                int act_index = 0;
                int count = 0;
                string line = Console.ReadLine();
                for (int j = 1; j < line.Length; j++)
                {
                    if (line[j] != line[act_index])
                        act_index = j;
                    else
                        count++;
                }
                Console.WriteLine(count);
            }
        }
    }
}