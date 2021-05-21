#Class07ArithmeticOperations

#PrecedenceOrder
# 01 => ( ) = Parenthesis
# 02 => ** = Potency
# 03 => * / // % = Multiplication, normalDivision,
# integralDivision && Module
# 04 => + - = Sum and subtraction

#ExampleExpression01
#5+3*2 == 11

#ExampleExpression02
#3*5+4**2 == 31

#ExampleExpression03
#3*(5+4)**2 == 243

#CalculusExamplesPart01

#PotencyExamples
# 01 - 4 ** 3 == 64
#02 - pow(4,3) == 64

#CalculusExamplesPart02
#25**(1/2) == 5.0
#127**(1/3) == 5.0265...

#OperationsExamples
#'Hi' + 'Brother' == 'HiBrother'

#'Point'*5 == 'PointPointPointPointPoint'

#'x' * 3 = 'xxx'

#print('A'*4) == AAAA

#CenteredTitle
gameTitle = input('Insert your favorite PC game')
print('The {:^20}'.format(gameTitle) +'title is awesome!')

#Values
val01 = int(input('Type the 1st value = '))
val02 = int(input('Now, type the 2nd value = '))
print('The multiplication is = {}, '.format(val01*val02), end='')
#The end='' command is used to allow the continuation
# between 02 print statements
#To break green print command lines = \n
print('the division is = {:.2f}'.format(val01/val02))
print('The sum is = {}'.format(val01+val02))
print('The subtraction is = {}'.format(val01-val02))

#Challenge05
# Build a software to capture a number,
# print its predecessor and its successor
val01 = int(input('Type a value = '))
#print('Method 01 = ')
#previous = val01 -1
#next = val01 +1
#print('Your input = {} | Next = {} | Previous = {}'.format(val01,next,previous))
print('Method 02 = ')
print('Input value = {} | Predecessor = {} | Successor = {}'.format(val01, (val01-1),(val01+1)))

#Challenge06
# Make a software capable of reading a number,
# print the double value, the triple value and
# the square root
print('========================================')
print('Challenge 06 - Double, Triple and square root')
input001 = int(input('Type an input = '))
#double = input001 *2
#triple = input001 *3
#sqrt = input001 ** (1/2)
print('Input = {} | Double = {} | Triple = {} | Square root = {}'.format(input001, (input001*2),(input001*3),pow(input001, (1/2))))

#Challenge07
# Build an app capable of receiving 02 mentions,
# calculate the average and show it on the print statement
print('========================================')
print('Challenge 07 - Average calculation')
avg01 = float(input('Type the 1st average = '))
avg02 = float(input('Now, type the 2nd average = '))
finalAvg = (avg01 + avg02) /2
print('1st average = {:.1f} | 2nd average = {:.1f} | Final average {:.1f}'.format(avg01,avg02,((avg01+avg02)/2)))

#Challenge08
# Make an app to receive a value in meters,
# print the input in centimeters and milimeters
print('========================================')
print('Challenge 08 - Meters details')
measurement = float(input('Type the measurement input = '))
km = measurement * 0.001
hm = measurement * 0.01
dam = measurement * 0.1
dm = measurement * 10
cm = measurement * 100
mm = measurement * 1000
print('Input = {} meters | Km = {:.4f} | Hm = {} | Dam = {:.2f} | Dm = {} | Cm = {} | Mm = {}'.format(measurement,km,hm,dam,dm,cm,mm))

#Challenge09
# Build a software to receive an input and print
# its multiplication table (From x1 to x10)
print('========================================')
print('Challenge 09 - Multiplication table')
value = int(input('Insert the sample value = '))
print('{} x 1 = {}'.format(value, (value*1)))
print('{} x 2 = {}'.format(value, (value*2)))
print('{} x 3 = {}'.format(value, (value*3)))
print('{} x 4 = {}'.format(value, (value*4)))
print('{} x 5 = {}'.format(value, (value*5)))
print('{} x 6 = {}'.format(value, (value*6)))
print('{} x 7 = {}'.format(value, (value*7)))
print('{} x 8 = {}'.format(value, (value*8)))
print('{} x 9 = {}'.format(value, (value*9)))
print('{} x 10 = {}'.format(value, (value*10)))


#Challenge10
# Create an app to receive the user cash availability
# and shows how many dollars can be purchased
# Consider = US$1.00 = R$5,24 (Updated in 2021/05/10 - 01:54)
print('========================================')
print('Challenge 10')

#Challenge11
# Build an app to receive the wall height, width,
# calculates the area and the paint quantity needed to paint the wall.
# Consider = 1L Paint can cover a 2m² area.
print('========================================')
print('Challenge 11')

#Challenge12
# Make a program to receive a product price and
# shows its new price considering 5% off
print('========================================')
print('Challenge 12')

#Challenge13
# Build a system to receive the worker salary
# and show a new salary with a magnification of 15%.
print('========================================')
print('Challenge 13')