# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Strings > Gemstones
# problem url: https://www.hackerrank.com/challenges/gem-stones/problem

n = int(input())

check = [0] * 26

stones_count = 0
gem_elements = 0
for i in range(n):
    stone = set(input())
    stones_count += 1
    for letter in stone:
        check[ord(letter) - 97] += 1

for c in check:
    if c == stones_count:
        gem_elements += 1
        
print(gem_elements)
