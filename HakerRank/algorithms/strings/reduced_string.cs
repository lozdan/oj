/*
author: Daniel Lozano
source: HAckerRank(https://www.hackerrank.com )
problem name: Algorithms > String > Super Reduced String
problem url: https://www.hackerrank.com/challenges/reduced-string/problem
*/

using System;

namespace HackerRank
{
    class Program
    {
        static void Main()
        {
            string line = Console.ReadLine();

            int count = 0;
            while (count < line.Length - 1)
            {
                if (line[count] == line[count + 1])
                {
                    line = line.Remove(count, 2);
                    count = -1;
                }
                count++;
            }

            if (String.IsNullOrEmpty(line))
                Console.Write("Empty String");
            else
                Console.Write(line);
        }
    }
}
