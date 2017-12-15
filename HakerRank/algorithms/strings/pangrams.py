# author: Daniel Lozano
# source: HAckerRank(https://www.hackerrank.com )
# problem name: Algorithms > Strings > Pangrams
# problem url: https://www.hackerrank.com/challenges/pangrams/problem

sentence = input().replace(" ", "")
alphabet = []

alphabet.append(sentence[0])
alphabet.append(sentence[0].lower())

count = 1
while len(alphabet) < 52 and count < len(sentence):
    if sentence[count] not in alphabet:
        if sentence[count] == sentence[count].upper():
            alphabet.append(sentence[count])
            alphabet.append(sentence[count].lower())
        else:
            alphabet.append(sentence[count])
            alphabet.append(sentence[count].upper())
    count += 1

if len(alphabet) == 52:
    print("pangram")
else:
    print("not pangram")
