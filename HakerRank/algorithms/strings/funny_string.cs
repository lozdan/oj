/*
author: Daniel Lozano
source: HackerRank(https://www.hackerrank.com )
problem name: Algorithms > Strings > Funny String
problem url: https://www.hackerrank.com/challenges/funny-string/problem
*/

using System;

namespace HackerRank
{
    class Program
    {
        static void Main()
        {
            int cases = int.Parse(Console.ReadLine());

            for (int j = 0; j < cases; j++)
            {
                string S = Console.ReadLine();

                bool funny = true;

                for (int i = 1; i < S.Length && funny; i++)

                    if (Math.Abs(S[i] - S[i - 1]) != Math.Abs(S[S.Length - i - 1] - S[S.Length - i - 1 + 1]))
                        funny = false;

                if (funny)
                    Console.WriteLine("Funny");
                else
                    Console.WriteLine("Not Funny");
            }
        }
    }
}
