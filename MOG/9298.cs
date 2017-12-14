/*
author: Daniel Lozano
source: MOG
problem name: Identifying tea
problem url: http://matcomgrader.com/problem/9298/identifying-tea/
*/

using System;

namespace MOG
{
    public class Program
    {
        static void Main()
        {
            int n = int.Parse(Console.ReadLine());
            int[] guesses = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

            int answer = 0;
            for (int i = 0; i < guesses.Length; i++)
            {
                if (guesses[i] == n)
                    answer++;
            }
            Console.WriteLine(answer);
        }
    }
}