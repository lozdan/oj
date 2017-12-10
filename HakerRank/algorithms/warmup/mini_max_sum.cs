/*
author: Daniel Lozano
source: HAckerRank(https://www.hackerrank.com )
problem name: Algorithms > Warmup > Mini-Max Sum
problem url: https://www.hackerrank.com/challenges/mini-max-sum/problem
*/

using System;
using System.Linq;

namespace HackerRank
{
    class Program
    {
        static void Main()
        {
            long[] line = Array.ConvertAll(Console.ReadLine().Split(), long.Parse);
            
            Array.Sort(line);

            long arraySum = line.Sum();
            long minValue = arraySum - line[4];
            long maxValue = arraySum - line[0];

            Console.Write(minValue + " " + maxValue);
        }
    }
}
