/*
author: Daniel Lozano
source: CodeFights ( https://codefights.com )
problem name: Challenge > rightmostRoundNumber
problem url: https://codefights.com/challenge/npgAxzzMjLxhaXwSM
*/

using System;

namespace CodeFights
{
    class Program
    {
        static void Main()
        {   
        }

        int rightmostRoundNumber(int[] inputArray) 
		{
		    int total = -1;
		    for (int i = 0; i < inputArray.Length; i++)
		    {
		        if(inputArray[i] % 10 == 0) total = i;
		    }
		    return total;
		}
    }
}
