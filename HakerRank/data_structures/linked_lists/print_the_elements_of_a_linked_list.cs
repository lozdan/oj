/*
author: Daniel Lozano
source: HackerRank ( https://www.hackerrank.com )
problem name: Data Structures: Linked Lists: Print the Elements of a Linked List
problem url: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
*/

public static void Print(Node head)
{
    while(head != null)
    {
        Console.WriteLine(head.Data);
        head = head.Next;
    }
}