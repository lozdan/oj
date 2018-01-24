# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Implementation > Designer PDF Viewer
# problem url: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

heights = list(map(int, input().split()))
word = input()

tallest = 0

for i in range(len(word)):
    if heights[ord(word[i]) - 97] > tallest:
        tallest = heights[ord(word[i]) - 97]
        
print(len(word) * tallest)
