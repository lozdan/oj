# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > nextSecond
# problem url: https://codefights.com/challenge/JKPD7LqN2fwkDWeFB

def nextSecond(currentTime):
    hours, minutes, seconds = currentTime
    seconds += 1
    if seconds < 60:
        return [hours, minutes, seconds]
    minutes += 1
    if minutes < 60:
        return [hours, minutes, 0]
    hours += 1
    if hours < 24:
        return [hours, 0, 0]
    return [0, 0, 0]
