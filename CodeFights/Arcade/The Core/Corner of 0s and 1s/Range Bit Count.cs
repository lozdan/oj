/*
author: Daniel Lozano
source: CodeFights
problem name: Arcade > The Core> Corner of 0s and 1s > Range Bit Count
problem url: https://codefights.com/arcade/code-arcade/corner-of-0s-and-1s/eC2Zxu5H5SnuKxvPT
*/

using System;

namespace CodeFights
{
    class Program
    {
        static void Main()
        {
        }

        static int rangeBitCount(int a, int b) 
        {
            int count1 = 0;
            for (int i = a; i <= b; i++)
            {
                count1+= Total1s(i);
            }
            return count1;
        }

        static int Total1s(int a)
        {
            int total = 0;
            for (int j = 0; j <= a; j++)
            {
                if ((a & (1 << j)) > 0) total++;
            }
            return total;
        }
    }
}
