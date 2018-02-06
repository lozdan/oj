# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > getMonthName
# problem url: https://codefights.com/challenge/FB5Y3tbqbvz4uy6b3/

import calendar
def getMonthName(mo):
    if calendar.month_abbr[mo % 13]:
        return calendar.month_abbr[mo % 13]
    else:
        return "invalid month"    
