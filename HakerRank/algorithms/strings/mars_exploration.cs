/*
author: Daniel Lozano
source: HackerRank(https://www.hackerrank.com )
problem name: Algorithms > Strings > Mars Exploration
problem url: https://www.hackerrank.com/challenges/mars-exploration/problem
*/

using System;

namespace HackerRank
{
    class Program
    {
        static void Main()
        {
            string s = Console.ReadLine();

            int changedLetters = 0;
            for (int i = 0; i < s.Length; i += 3)
            {
                if (s[i] != 'S')
                    changedLetters++;
                if (s[i + 1] != 'O')
                    changedLetters++;
                if (s[i + 2] != 'S')
                    changedLetters++;
            }
            
            Console.WriteLine(changedLetters);
        }
    }
}
