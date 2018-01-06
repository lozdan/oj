# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Arcade > The Core> Corner of 0s and 1s > Second-Rightmost Zero Bit
# problem url: https://codefights.com/arcade/code-arcade/corner-of-0s-and-1s/9nSj6DgqLDsBePJha

def secondRightmostZeroBit(n):
    return 1 << [i for i in range(32) if n & (1 << i) == 0][1]
