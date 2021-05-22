#Importing the math bookshelf
#import math
#numInput = int(input('Please, type a number = '))
#sqRoot = math.sqrt(numInput)
#print('The {} square root is = {:.3f}'.format(numInput,sqRoot))
#print('The {} square root + ceiling is = {:.3f}'.format(numInput,math.ceil(sqRoot)))
#print('The {} square root + floor is = {:.3f}'.format(numInput,math.floor(sqRoot)))

#Or also =
#from math import sqrt || from math import sqrt, floor
#print('The {} square root + floor is = {:.3f}'.format(numInput,floor(sqRoot)))

#Importing random bookshelf
#import random
#sampleInput = random.randint(1,100)
#print(sampleInput)

#import emoji
#print(emoji.emojize('Hello, Legend coders :earth_americas:',use_aliases=True))

#Challenge16
#Create a software to receive any royal number (1,23 (Example))
#and output its integer value (1 (Example))
print('==================================')
print('Challenge 16 - Floor value configurator')
print('Form 01 = ')
#import math
#sampleVal01 = float(input('Type the 1st value = '))
#print('Typed integer01 = {} | Integer01 portion = {}'.format(sampleVal01, math.trunc(sampleVal01)))
print('Form 02 = ')
from math import trunc
sampleVal02 = float(input('Type the 2nd value = '))
print('Typed integer02 = {} | Integer02 portion = {}'.format(sampleVal02,trunc(sampleVal02)))

print('Form 03 = ')
sampleVal03 = float(input('Type the 3rd value = '))
print('Typed integer03 = {} | Integer03 portion {}'.format(sampleVal03,int(sampleVal03)))

#Challenge17
#Create a software to receive the triangle opposite and adjacent
# cathetes measurement, make the needed calculuses
# and shows the hypotenuse measurement
print('==================================')
print('Challenge 17 - Hypotenuse calculator')
opCa = float(input('Insert the opposite cathete value = '))
adjCa = float(input('Now, type the adjacent cathete value = '))
print('Opposite cathete = {} | Adjacent cathete = {} | Hypotenuse = {:.2f}'.format(opCa, adjCa, (opCa **2 + adjCa **2)**(1/2)))

#Challenge18
#Create a software to receive the angle value
# and show its sine, cosine and tangent
print('==================================')
print('Challenge 18 - Sine, cosine and tangent angle calculator')

#Challenge19
# Create an app to read the students names and show
# one of these names on the screen
print('==================================')
print('Challenge 19 - Selected student (Sort)')

#Challenge20
# Create an app to configure the students presentation order
# by reading 05 students names and showing the sorted presentation order
print('==================================')
print('Challenge 20 - Selected student (Sort)')

#Challenge21
# Create a software to open and run a mp3 audio file
print('==================================')
print('Challenge 21 - MP3 player')
