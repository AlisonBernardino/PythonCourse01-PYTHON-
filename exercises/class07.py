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


#Challenge06
# Make a software capable of reading a number,
# print the double value, the triple value and
# the square root

#Challenge07
# Build an app capable of receiving 02 mentions,
# calculate the average and show it on the print statement

#Challenge08
# Make an app to receive a value in meters,
# print the input in centimeters and milimeters

#Challenge09
# Build a software to receive an input and print
# its multiplication table (From x1 to x10)

#Challenge10
# Create an app to receive the user cash availability
# and shows how many dollars can be purchased
# Consider = US$1.00 = R$5,24 (Updated in 2021/05/10 - 01:54)

#Challenge11
# Build an app to receive the wall height, width,
# calculates the area and the paint quantity needed to paint the wall.
# Consider = 1L Paint can cover a 2m² area.

#Challenge12
# Make a program to receive a product price and
# shows its new price considering 5% off

#Challenge13
# Build a system to receive the worker salary
# and show a new salary with a magnification of 15%.