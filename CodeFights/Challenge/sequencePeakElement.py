# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > sequencePeakElement
# problem url: https://codefights.com/challenge/GMkfrHjyKvf2yjhy8

def sequencePeakElement(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i + 1]:
            return sequence[i]
