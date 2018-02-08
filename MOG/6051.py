# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Anton and Letters
# problem url: http://matcomgrader.com/problem/6051/anton-and-letters/

line = input()

letters_set = set()
for i in range(2, len(line), 3):
    letters_set.add(line[i])

print(len(letters_set))
