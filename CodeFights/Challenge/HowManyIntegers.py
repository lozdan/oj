# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > HowManyIntegers
# problem url: https://codefights.com/challenge/YKsT8AQDYrBvfHJFx

def HowManyIntegers(N):
     count = 0
     for i in range(1, N):
          x = 0
          i = str(i)
          for j in range(len(i)):
               if "0" == i[j] or "4" == i[j] or '7' == i[j]:
                    x += 1
          if x == len(i):
               count += 1
     return count
          