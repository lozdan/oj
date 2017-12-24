/*
author: Daniel Lozano
source: HackerRank(https://www.hackerrank.com )
problem name: Algorithms > Implementation > Between Two Sets
problem url: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
*/

using System;

namespace HackerRank
{
    class Program
    {
        static void Main()
        {
            int n = int.Parse(Console.ReadLine());
            string[] tempGames = Console.ReadLine().Split();
            int[] games = Array.ConvertAll(tempGames, int.Parse);
            
            int maxScore = games[0];
            int minScore = games[0];

            int maxChanges = 0;
            int minChanges = 0;
            for (int i = 1; i < n; i++)
            {
                if (games[i] > maxScore)
                {
                    maxChanges++;
                    maxScore = games[i];
                }                    
                else if (games[i] < minScore)
                {
                    minChanges++;
                    minScore = games[i];
                }
                    
            }

            Console.Write(maxChanges + " " + minChanges);            
        }
    }
}