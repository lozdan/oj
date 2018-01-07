/*
author: Daniel Lozano
source: HackerRank(https://www.hackerrank.com )
problem name: Algorithms > Bit Manipulation > Lonely Integer
problem url: https://www.hackerrank.com/challenges/lonely-integer/problem
*/

using System;

class HackerRank {
    static void Main() 
    {
        int n = int.Parse(Console.ReadLine());
        string[] temp = Console.ReadLine().Split();
        int[] numbers = Array.ConvertAll(temp, int.Parse);
        Array.Sort(numbers);
        if (n == 1) Console.Write(numbers[0]);
        
        for (int i = 1; i < n; i++)
        {
            if (i == n - 1) 
            {
                Console.Write(numbers[i]);
                break;
            }
            if (numbers[i] != numbers[i-1] && numbers[i] != numbers[i+1])
            {
                Console.Write(numbers[i]);
                break;
            }
        }
    }
}
