#Class06A
# Ex001IntegerSum
num001 = int(input('Please, type the 1st value = '))
#print(type(num001))
num002 = int(input('Now, insert the 2nd value = '))
sumValues = num001 + num002
print('The sum between {00} and {01} is = {02} '.format(num001,num002,sumValues))

#Ex002NumericChecker
number001 = input('Type the 3rd value = ')
print(number001.isnumeric())

#Ex003AlphaChecker
number002 = input('Type the 4th input = ')
print(number002.isalpha())

#Ex004AlphanumericChecker
number003 = input('Insert the 5th value = ')
print(number003.isalnum())

#Ex005UppercaseChecker
number004 = input('Insert the 6th value = ')
print(number004.isupper())

#Challenge003Ex001
# Create a program with the following capacity:
# 01 => Read 02 numbers
# 02 => Show the sum between these numbers
print('Challenge003Ex001 = Int values sum')
value01 = int(input('Insert the 7th value = '))
value02 = int(input('Now, insert the 8th value = '))
challenge003Sum = value01 + value02
print('The challenge003Ex001 sum is = {} '.format(challenge003Sum))

#Challenge003Ex002
# Create another program capable of =
# 01 => Reading the keyboard input
# 02 => Show the input primitive type
# 03 => And show all the possible informations
print('Challenge003Ex002DataAnalyzer')
c003Ex002Input = input('Please, insert a value = ')
print('The input data type is = ',type(c003Ex002Input))
print('Does this string has only blank spaces?',c003Ex002Input.isspace())
print('Is this input a number?',c003Ex002Input.isnumeric())
print('Is this input alphabetic?',c003Ex002Input.isalpha())
print('Is this input alphanumeric?',c003Ex002Input.isalnum())
print('Is this input in uppercase?',c003Ex002Input.isupper())
print('Is this input in lowercase?',c003Ex002Input.islower())
print('Is this input capitalized?',c003Ex002Input.istitle())
