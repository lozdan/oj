def makeArrayConsecutive2(statues):
    statues.sort()
    res = 0
    for i in range(statues[-1] - statues[0]):
        if statues[i] + 1 != statues[i + 1]:
            statues.insert(i+1, statues[i] + 1)
            res += 1
    return res
