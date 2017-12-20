/*
author: Daniel Lozano
source: HackerRank ( https://www.hackerrank.com )
problem name: Data Structures: Linked Lists: Insert a node at the head of a linked list
problem url: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
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
            node.Next = head;
            return node;
        }

        public static void Main()
        {
           
        }
    }
}