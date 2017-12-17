# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: metroCard
# problem url: https://codefights.com/arcade/code-arcade/at-the-crossroads/J7PQDxpWqhx7HrvBZ

def metroCard(lastNumberOfDays):
    if lastNumberOfDays == 28:
        return [31]
    elif lastNumberOfDays == 30:
        return [31]
    else:
        return [28, 30, 31]