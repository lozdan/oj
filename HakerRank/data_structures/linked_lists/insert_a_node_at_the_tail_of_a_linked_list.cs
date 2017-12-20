/*
author: Daniel Lozano
source: HackerRank ( https://www.hackerrank.com )
problem name: Data Structures: Linked Lists: Insert a Node at the Tail of a Linked List
problem url: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
*/

using System;

namespace HackerRank
{
    public class Program
    {
        public class Node
        {
            public int Data;
            public Node Next;
        }

        public static Node Insert(Node head, int x)
        {
            Node node = new Node() { Data = x };
            if (head == null)
                return node;
            Node current = head;
            while (current.Next != null)
                current = current.Next;
            current.Next = node;
            return head;
        }

        public static void Main()
        {
           
        }
    }
}