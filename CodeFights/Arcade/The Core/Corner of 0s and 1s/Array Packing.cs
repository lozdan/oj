/*
author: Daniel Lozano
source: CodeFights
problem name: Arcade > The Core> Corner of 0s and 1s > Array Packing
problem url: https://codefights.com/arcade/code-arcade/corner-of-0s-and-1s/KeMqde6oqfF5wBXxf
*/

namespace CodeFights
{
    class Program
    {
        static void Main()
        {
        }

        static int arrayPacking(int[] a)
        {
            int ans = 0;
            for (int i = 0; i < a.Length; i++)
            {
                ans = ans | (a[i] << 8 * i);
            }
            return ans;
        }
    }
}
