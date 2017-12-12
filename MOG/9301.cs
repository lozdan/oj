/*
author: Daniel Lozano
source: MOG
problem name: Automated Checking Machine
problem url: http://matcomgrader.com/problem/9301/automated-checking-machine/
*/

using System;

namespace MOG
{
    class Solution
    {
        static void Main()
        {
            string[] connection1 = Console.ReadLine().Split();
            string[] connection2 = Console.ReadLine().Split();

            int count = 0;
            while(count < connection1.Length && connection1[count] != connection2[count])
                count++;

            if (count < connection1.Length)
                Console.WriteLine("N");
            else
                Console.WriteLine("Y");
        }
    }
}
