/*
 * author: Daniel Lozano
 * source: HackerRank ( https://www.hackerrank.com )
 * problem name: Data Structures: Trees: Tree: Height of a Binary Tree
 * problem url: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
 */

static int height(Node root)
{
    if (root != null)
    {
        int l = height(root.left);
        int r = height(root.right);
        if (l > r)
            return l + 1;
        else
    		return r + 1;
	}
	return -1;
}