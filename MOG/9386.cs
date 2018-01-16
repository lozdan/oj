/*
author: Daniel Lozano
source: MOG
problem name: Jingle Composing
problem url: http://matcomgrader.com/problem/9386/jingle-composing/
*/

using System;

namespace MOG
{    
    class Solution
    {
        static void Main()
        {
            while (true)
            {
                string notes = Console.ReadLine();
                if (notes == "*") break;

                int total = 0;
                int rigthDuration = 0;
                for (int i = 1; i < notes.Length; i++)
                {
                    if (notes[i] == 'W')
                        total += 64;

                    else if (notes[i] == 'H')
                        total += 32;

                    else if (notes[i] == 'Q')
                        total += 16;

                    else if (notes[i] == 'E')
                        total += 8;

                    else if (notes[i] == 'S')
                        total += 4;

                    else if (notes[i] == 'T')
                        total += 2;

                    else if (notes[i] == 'X')
                        total += 1;
                    else
                    {
                        if (total == 64)
                            rigthDuration++;
                        total = 0;
                    }
                }
                Console.WriteLine(rigthDuration);
            }
        }       
    }
}