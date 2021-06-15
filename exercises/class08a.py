# Python course 01 - Gustavo Guanabara
# ATTENTION = Check the commented
# examples/exercises lines to avoid execution errors

# Importing the math bookshelf
# import math
# numInput = int(input('Please, type a number = '))
# sqRoot = math.sqrt(numInput)
# print('The {} square root is = {:.3f}'.format(numInput,sqRoot))
# print('The {} square root + ceiling is = {:.3f}'.format(numInput,math.ceil(sqRoot)))
# print('The {} square root + floor is = {:.3f}'.format(numInput,math.floor(sqRoot)))

# Or also =
# from math import sqrt || from math import sqrt, floor
# print('The {} square root + floor is = {:.3f}'.format(numInput,floor(sqRoot)))

# Importing random bookshelf
# import random
# sampleInput = random.randint(1,100)
# print(sampleInput)

# import emoji
# print(emoji.emojize('Hello, Legend coders :earth_americas:',use_aliases=True))

# Challenge16
# Create a software to receive any royal number (1,23 (Example))
# and output its integer value (1 (Example))
# print('==================================')
# print('Challenge 16 - Floor value configurator')
# print('Form 01 = ')
# import math
# sampleVal01 = float(input('Type the 1st value = '))
# print('Typed integer01 = {} | Integer01 portion = {}'.format(sampleVal01, math.trunc(sampleVal01)))
# print('Form 02 = ')
# from math import trunc
# sampleVal02 = float(input('Type the 2nd value = '))
# print('Typed integer02 = {} | Integer02 portion = {}'.format(sampleVal02,trunc(sampleVal02)))

# print('Form 03 = ')
# sampleVal03 = float(input('Type the 3rd value = '))
# print('Typed integer03 = {} | Integer03 portion {}'.format(sampleVal03,int(sampleVal03)))

# Challenge17
# Create a software to receive the triangle opposite and adjacent
# cathetes measurement, make the needed calculuses
# and shows the hypotenuse measurement
# print('==================================')
# print('Challenge 17 - Hypotenuse calculator')
# opCa = float(input('Insert the opposite cathete value = '))
# adjCa = float(input('Now, type the adjacent cathete value = '))
# print('Opposite cathete = {} | Adjacent cathete = {} | Hypotenuse = {:.2f}'.format(opCa, adjCa, (opCa **2 + adjCa **2)**(1/2)))

# Challenge18
# ATTENTION = Check the commented lines to avoid execution errors
# Create a software to receive the angle value
# and show its sine, cosine and tangent
# import math
# print('==================================')
# print('Challenge 18 - Sine, cosine and tangent angle calculator')
# angle = float(input('Please, type the desired angle = '))
# sine = math.sin(math.radians(angle))
# cossine = math.cos(math.radians(angle))
# tangent = math.tan(math.radians(angle))
# print('Typed angle = {}º | Sine = {:.2f} | Cossine = {:.2f} | Tangent = {:.2f}'.format(angle, sine, cossine, tangent))
# OR
# from math import radians, sin, cos, tan
# sine = sin(radians(angle))
# cossine = cos(radians(angle))
# tangent = tan(radians(angle))

# Challenge19
# Create an app to read the students names and show
# one of these names on the screen
print('==================================')
print('Challenge 19 - Selected student (Sort)')
# import random (And type .random during "random" method use)
# OR
# from random import choice
# nameIndex = 0
# name01 = str(input('Insert the student 0{} name = '.format(nameIndex+1)))
# name02 = str(input('Now, type the student 0{} name = '.format(nameIndex+2)))
# name03 = str(input('Please, type the student 0{} name = '.format(nameIndex+3)))
# name04 = str(input('Insert the student 0{} name = '.format(nameIndex+4)))
# name05 = str(input('And now, insert the student 0{} name = '.format(nameIndex+5)))
# studentsList = [name01, name02, name03, name04, name05]
# chosenStudent = choice(studentsList)
# print('The chosen student was {}'.format(chosenStudent))

# Challenge20
# Create an app to configure the students presentation order
# by reading 05 students names and showing the sorted presentation order
# print('==================================')
# print('Challenge 20 - Names presentation order (Sort)')
# studentNameIndex = 0
# import random
# student01 = str(input('Type the name 0{} = '.format(studentNameIndex+1)))
# student02 = str(input('Now, type the name 0{} = '.format(studentNameIndex+2)))
# student03 = str(input('Please, type the name 0{} = '.format(studentNameIndex+3)))
# student04 = str(input('Type the name 0{} = '.format(studentNameIndex+4)))
# student05 = str(input('And now, type the name 0{} = '.format(studentNameIndex+5)))
# presentationList = [student01, student02, student03, student04, student05]
# random.shuffle(presentationList)
# print('The presentation order will be = {}'.format(presentationList))


# Challenge21
# Create a software to open and run a mp3 audio file
print('==================================')
print('Challenge 21 - MP3 player')
import pygame
pygame.init()
pygame.mixer.music.load('sampleSong.mp3')
pygame.mixer.music.play()
pygame.event.wait()
