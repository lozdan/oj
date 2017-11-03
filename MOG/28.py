# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Snail
# problem url: http://matcomgrader.com/problem/28/snail/
# date: 6/2/2017

def number_of_days(A, B, V):
    result = (V - B) // (A - B)
    if (V - B) % (A - B) != 0:
        return result + 1
    return result



arr = [int(i) for i in input().split()]
print(number_of_days(arr[0], arr[1], arr[2]))