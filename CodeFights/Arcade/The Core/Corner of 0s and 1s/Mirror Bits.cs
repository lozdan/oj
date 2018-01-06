/*
author: Daniel Lozano
source: CodeFights
problem name: Arcade > The Core> Corner of 0s and 1s > Mirror Bits
problem url: https://codefights.com/arcade/code-arcade/corner-of-0s-and-1s/e3zfPNTwTa9qTQzcX
*/

namespace CodeFights
{
    class Program
    {
        static void Main()
        {
        }

        static int mirrorBits(int a)
        {
            int mirror = 0;
            while (a > 0)
            {
                mirror += a & 1;
                a = a >> 1;
                mirror = mirror << 1;
            }
            return mirror >> 1;
        }
	}
}
