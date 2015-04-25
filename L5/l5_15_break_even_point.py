__author__ = 'miroslav'

import math

million = 1000000

def Q(state, action, U):
    if action == 'hold':
        return U(state + 1*million)
    if action == 'gamble':
        return U(state + 3*million) * .5 + U(state) * .5

U = math.log10

print Q(million, 'hold', U)
print Q(million, 'gamble', U)