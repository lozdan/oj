/*
author: Daniel Lozano
source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
problem name: Formacion
problem url: http://matcomgrader.com/problem/51/formacion/
*/
using System;

namespace MOG
{
    class Solution
    {
        static void Main()
        {
            long n = long.Parse(Console.ReadLine());
            long[] height = new long[n];

            long fitoPosition = 0;

            for (long i = 0; i < n; i++)
            {
                height[i] = long.Parse(Console.ReadLine());
                if (height[i] < height[fitoPosition])
                    fitoPosition = i;
            }

            Console.WriteLine(fitoPosition + 1);

            Array.Sort(height);

            for (long i = 0; i < n; i++)
            {
                Console.Write(height[i]);
                Console.Write(" ");
            }
        }
    }
}
