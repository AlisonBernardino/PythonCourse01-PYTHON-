#Class 09 - String manipulation
# String cut technique
sentence = 'Welcome to Python world'
#My custom examples
# Example 00 - Based on course example
print(sentence[1])
print(sentence[0:7])
print(sentence[8:])
print(sentence[2:13:2])
print(sentence[1::3])

#To write large sentences
largeSentence = """This is an example to print a large text on the screen. 
To write this kind of text, you can use the composed quotation marks.
 Just write it 03 times to open the text typing area and after 
 finishing the text, type the 03 elements again."""

#To print the largeSentence
print(largeSentence)

#To count the "A" letters number inside the text
print(largeSentence.count('a'))

#To gather the word length index
# 01 - Considering spaces quantity
print(len(largeSentence))

# 02 - Discarding the spaces quantity
print(len(largeSentence) - largeSentence.count(" "))

#To replace a word for another
print(largeSentence.replace('marks','"items"'))

#To find a word inside the large sentence
print(largeSentence.find('a'))

#To split the sentence in smaller sentences
print(largeSentence.split())

#To print a sentence inside the largeSentence string vector
print(largeSentence[15])

#Challenge 022 - Word analyzer
#Create a software to read someone's complete name
#and shows:
# 01 - Name in uppercase
# 02 - Nname in lowercase
# 03 - Name length quantity (Discarding spaces)
# 04 - First name letters quantity
nameInput = str(input('Type your entire name = ')).strip()
print('Analyzing your name...')
print('Name in uppercase = {}'.format(nameInput.upper()))
print('Name in lowercase = {}'.format(nameInput.lower()))
print('Full name letters quantity = {}'.format(len(nameInput) - nameInput.count(' ')))
print('First name letters quantity = {}'.format(nameInput.find(' ')))
splittedName = nameInput.split()
print('First name = {} | Letters quantity = {}'.format(splittedName[0], len(splittedName[0])))

#Challenge 023 - Digits separator
# Make an app to read the numbers between 0-9999
# and display all the digits separately

# Example:
# Type a number = 1834

# Output =
# Units ==
# Hundreds ==
# Thousands ==


# Challenge 24 - Word detector
# Create a software to read a city name
# and identify the "York" word existance
# inside the city name

#Challenge 25 - Name part identifier
# Make an app to check if the name has
# the "Silva" word

# Challenge 26 - Word analyzer v2.0
# Build an application to read a sentence
# and shows:
# 01 - The number of "H" letters
# 02 - The first "H" letter index inside the vector
# 03 - The last "H" letter index inside the vector

# Challenge 27 - Full name splitter
# Make an app to read someone's full name
# and show the first name separated from the
# other names

# Example =
# Input = Alison Francisco Bernardino
# Output =
# First name = Alison
# Middle name = Francisco
# Last name = Bernardino
