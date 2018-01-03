# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > isPangram
# problem url: https://codefights.com/challenge/JbpJhJYDovKY5TeqK

def isPangram(sentence):
    letters = set()
    sentence = sentence.lower()
    for c in sentence:
        if c not in letters and c.isalpha():
            letters.add(c)
    return len(letters) == 26
    