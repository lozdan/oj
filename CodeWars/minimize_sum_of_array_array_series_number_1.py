# author: Daniel Lozano
# source: CodeWars ( http://www.codewars.com )
# problem name: Kata > Minimize _sum_Of_array_(Array_Series_#1)
# problem url: https://www.codewars.com/kata/minimize-sum-of-array-array-series-number-1

def min_sum(arr):
    arr.sort()
    back_index = len(arr) - 1
    min_total = 0
    for i in range(len(arr)//2):
        min_total += arr[i] * arr[back_index]
        back_index -= 1
    return min_total
    