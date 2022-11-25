import numpy as np
def partof_day(hour=int):
    if hour<0 or hour>23:
        return(f'{hour} is not possible, please try entering a number between 0-23 (inclusive)')
    elif hour < 7:
        return'night'
    elif hour < 13:
        return'morning'
    elif hour < 19:
        return'afternoon'
    elif hour < 24:
        return'evening'
        
"""TEST"""
for i in np.arange(-1,25):
    if i in np.arange(24):
        print(f'Hour {i} is in the {partof_day(i)}')
    else:
        print(partof_day(i))