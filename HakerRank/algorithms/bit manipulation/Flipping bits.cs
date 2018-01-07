/*
author: Daniel Lozano
source: HackerRank(https://www.hackerrank.com )
problem name: Algorithms > Bit Manipulation > Flipping bits
problem url: https://www.hackerrank.com/challenges/flipping-bits/problem
*/

using System;

class HackerRank 
{
    static void Main()
    {
        uint cases = uint.Parse(Console.ReadLine());
        for (int i = 0; i < cases; i++)
        {
            uint number = uint.Parse(Console.ReadLine());
            Console.WriteLine(~number);
        }        
    }
}
