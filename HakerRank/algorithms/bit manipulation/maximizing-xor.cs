/*
author: Daniel Lozano
source: HackerRank(https://www.hackerrank.com )
problem name: Algorithms > Bit Manipulation > Maximizing XOR
problem url: https://www.hackerrank.com/challenges/maximizing-xor/problem
*/

using System;

class HackerRank {
    static void Main()
    {
        int l = int.Parse(Console.ReadLine());
        int r = int.Parse(Console.ReadLine());
        int total = l ^ l;
        for (int i = l; i <= r; i++)
        {
            for (int j = l; j <= r; j++)
            {
                int operation = i ^ j;
                if (total < operation) total = i ^ j;
            }
        }
        Console.Write(total);
    }
}
