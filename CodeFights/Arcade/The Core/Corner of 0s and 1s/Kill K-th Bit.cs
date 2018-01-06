/*
author: Daniel Lozano
source: CodeFights
problem name: Arcade > The Core> Corner of 0s and 1s > Kill K-th Bit
problem url: https://codefights.com/arcade/code-arcade/corner-of-0s-and-1s/b5z4P2r2CGCtf8HCR
*/

int killKthBit(int n, int k)
{
  return n&(~(1 << (k - 1)));
}
