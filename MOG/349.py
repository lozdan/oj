# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Generando cadena homogénea
# problem url: http://matcomgrader.com/problem/349/fracciones-irreducibles/

n, d = list(map(int, input().split()))

divisor = max(n, d)
while divisor > 1:
    if n % divisor == 0 and d % divisor == 0:
        n = n // divisor
        d = d // divisor
    divisor -= 1

print(n, d)

