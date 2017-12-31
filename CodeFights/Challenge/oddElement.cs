/*
author: Daniel Lozano
source: CodeFights ( https://codefights.com )
problem name: Challenge > oddElement
problem url: https://codefights.com/challenge/nSkvZBaXbb5fngBRs
*/

using System;

namespace CodeFights
{
    class Program
    {
        static void Main()
        {
            
        }

        int oddElement(int[] a)
        {
            int x = a[a.Length - 1];
            Array.Sort(a);
            for (int i = 0; i < a.Length - 1; i += 2)
            {
                if (a[i] != a[i + 1]) return a[i];
            }
            return x;
        }
    }
}