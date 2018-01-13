/*
author: Daniel Lozano
source: CodeFights ( https://codefights.com )
problem name: Challenge > bestFriendNames
problem url: https://codefights.com/challenge/RTHN8Lgek9PTyPRBX
*/

namespace CodeFigths
{    
    class Solution
    {
        static void Main()
        {
        }

        static bool bestFriendNames(string name1, string name2)
        {
            if (sumCal(name1.ToLower().Replace(" ", "")) == sumCal(name2.ToLower().Replace(" ", "")))
            {
                return true;
            }
            return false;
        }

        static int sumCal(string name)
        {
            int total = 0;
            for (int i = 0; i < name.Length; i++)
            {
                total += name[i] - 96;
            }
            return total;
        }

    }
}