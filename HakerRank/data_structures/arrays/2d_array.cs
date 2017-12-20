/*
author: Daniel Lozano
source: HackerRank ( https://www.hackerrank.com )
problem name: Data Structures: Arrays: 2D Array - DS
problem url: https://www.hackerrank.com/challenges/2d-array/problem
*/

using System;

namespace HackerRank
{
    public class Resolution
    {
        public static void Main()
        {
            int[,] matrix = new int[6, 6];
            for (int i = 0; i < 6; i++)
            {
                int[] temp_matrix = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
                for (int j = 0; j < 6; j++)
                {
                    matrix[i, j] = temp_matrix[j];
                }
            }
            Console.Write(Solution(matrix));

        }
        public static int Solution(int[,] lines)
        {
            int sum = -9999999;
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    int currentSum = lines[i, j] + lines[i, j + 1] + lines[i, j + 2] + lines[i + 1, j + 1] + lines[i + 2, j] + lines[i + 2, j + 1] + lines[i + 2, j + 2];
                    if (currentSum > sum)
                        sum = currentSum;
                }
            }
            return sum;
        }
        
    }
}
