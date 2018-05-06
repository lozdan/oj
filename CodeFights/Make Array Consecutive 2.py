# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: makeArrayConsecutive2
# problem url: https://codefights.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC

def makeArrayConsecutive2(statues):
    statues.sort()
    res = 0
    for i in range(statues[-1] - statues[0]):
        if statues[i] + 1 != statues[i + 1]:
            statues.insert(i+1, statues[i] + 1)
            res += 1
    return res
