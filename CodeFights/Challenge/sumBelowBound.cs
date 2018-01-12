/*
author: Daniel Lozano
source: CodeFights ( https://codefights.com )
problem name: Challenge > sumBelowBound
problem url: https://codefights.com/challenge/sgcZbafiFjcQq3rnf
*/

namespace CodeFigths
{    
    class Solution
    {
        static void Main()
        {
        }

        static int sumBelowBound(int bound)
        {
            int carry = 1;
            int count = 2;
            while (carry <= bound)
            {
                carry += count;
                count++;
            }
            return count - 2;
        }
    }
}
