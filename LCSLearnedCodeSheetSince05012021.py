# LCS - Learned Code Sheet - Since 05/01/2021

Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hi, PythonWorld!')
Hi, PythonWorld!
>>> print(Hello, PythonCoders!)
SyntaxError: invalid syntax
>>> print(8+10)
18
>>> print('2'+'3')
23
>>> 7+4
11
>>> print('Hello",5)
      
SyntaxError: EOL while scanning string literal
>>> print('Hello',5)
Hello 5
>>> print('Welcome aboard',XLR8)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print('Welcome aboard',XLR8)
NameError: name 'XLR8' is not defined
>>> print('Welcome aboard,',X)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print('Welcome aboard,',X)
NameError: name 'X' is not defined
>>> print('Welcome aboard',3188)
Welcome aboard 3188
>>> name - 'Vegas'
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    name - 'Vegas'
NameError: name 'name' is not defined

print('Hello, Coders!')

>>> name = input('What is your name?')
What is your name?Alison
>>> age = input('What is your age?')
What is your age?25
>>> weight = input('What is your weight?')
What is your weight?56.4
>>> print(name,age,weight)
Alison 25 56.4


# Test 01, 02 and 03 scripts

# Test 01 - Name, age and formationLevel
name = input('What is your name?')
age = input('What is your age?')
formationLevel = input('What is your formation level?')
print('Nice to meet you, Mr. ',name + ', your age is', age + ' and your formation level is',formationLevel)

# Test 02 - Formatted born date
month = input('Please, insert the month: ')
day = input('Now, insert the day: ')
year = input('To finish this questionnaire, insert the year: ')
print('You were born in',year,month,day + ',right?') 

# Test 03 - Items sum
