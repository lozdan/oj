/*
author: Daniel Lozano
source: HackerRank(https://www.hackerrank.com )
problem name: Algorithms > Bit Manipulation > Sum vs XOR
problem url: https://www.hackerrank.com/challenges/sum-vs-xor/problem
*/

using System;

class HackerRank {
    static void Main() 
    {
        long x = long.Parse(Console.ReadLine());
            if (x == 0)
            {
                Console.Write(1);
                return;
            }
            int totalZeros = 0;
            int count = 0;
            while (x != 0)
            {
                if ((x & 1) == 0) totalZeros++;
                count++;
                x = x >> 1;
            }
            Console.WriteLine(1L << totalZeros);
    }
}
