### Modules ###

import module as m
import module
import math

print('1 - Import with alias: ',m.multiple_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print('2 - Import without alias:', module.multiple_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


from module import sum, multiple_sum

print('3 - Import specific functions: ')
print('\t', multiple_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print('\t', sum(1, 2))


#import module as m
from math import pi as pivote

print('4 - Import specific functions with alias: ', pivote)

