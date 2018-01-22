# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Feynman
# problem url: http://matcomgrader.com/problem/9393/feynman/

while True:
    n = int(input())
    
    if n == 0:
        break
        
    print(n * (n + 1) * (2 * n + 1) // 6)
        