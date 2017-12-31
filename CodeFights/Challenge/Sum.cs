/*
author: Daniel Lozano
source: CodeFights ( https://codefights.com )
problem name: Challenge > Sum
problem url: https://codefights.com/challenge/k65tsTbnyL6Jamzhs
*/

using System;

namespace CodeFights
{
    class Program
    {
        static void Main()
        {
            
        }

        int Sum(int a, int b)
        {
            int carry = 0;
            for (int i = a; i <= b; i++) carry += i;
            return carry;
        }
    }
}
