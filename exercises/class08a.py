#Importing the math bookshelf
import math
numInput = int(input('Please, type a number = '))
sqRoot = math.sqrt(numInput)
print('The {} square root is = {:.3f}'.format(numInput,sqRoot))
print('The {} square root + ceiling is = {:.3f}'.format(numInput,math.ceil(sqRoot)))
print('The {} square root + floor is = {:.3f}'.format(numInput,math.floor(sqRoot)))

#Or also =
#from math import sqrt || from math import sqrt, floor
#print('The {} square root + floor is = {:.3f}'.format(numInput,floor(sqRoot)))

#Importing random bookshelf
import random
sampleInput = random.randint(1,100)
print(sampleInput)

import emoji
