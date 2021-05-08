import math
import random

chances=5
num=random.randint(0,10)
while chances>0:
    number=int(input('gess the computers number'))
    chances=chances-1
    if number==num:
        print('you won the game')
        break
    elif number>num:
        print('gess a lower number')
    else:
        print('gess ahigher number')
