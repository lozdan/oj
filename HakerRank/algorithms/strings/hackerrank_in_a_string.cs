/*
author: Daniel Lozano
source: HackerRank(https://www.hackerrank.com )
problem name: Algorithms > Strings > HackerRank in a String!
problem url: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
*/

using System;

namespace HackerRank
{
	class Program
	{
	    static void Main()
	    {
	        int queries = int.Parse(Console.ReadLine());
	        string check = "hackerrank";
	        for (int i = 0; i < queries; i++)
	        {
	            string word = Console.ReadLine();
	            int count = 0;
	            for (int j = 0; j < word.Length && count < 10; j++)
	            {
	                if (check[count] == word[j])
	                    count++;
	            }
	            if (count == 10)
	                Console.WriteLine("YES");
	            else
	                Console.WriteLine("NO");
	        }
	    }
	}
}