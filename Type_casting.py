# -*- coding: utf-8 -*-
"""TYPE CASTING.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GP7pMjoE4EcyudsQhVLNzsGHOr-85i7B
"""

# 1. Implicit type conversion: Python automatically convert datatype one to an other data type

int(2.3) #cast from float to int

int(2.3, 3.0)

int(True) #cast from bool to int

int(False)

True + True

int(1+2j)

int('10')

float(10)

float(True)

float(False)

float('10')

float('ten')

True + True

complex(10)

complex(10, 20)

complex(2.3)

complex(2.3, 4)

complex(True, True)

complex(False)

complex('10')

complex('10', '20')

a = 5+ 5 # integer
print(a)

b = 5.5 + 5
print(b) # float

5+6+7j

c = True + True # boolean
print(c) # integer

d = True + False # boolean
print(d) # integer

a = 2+7j + 1+2j # complex
print(a) # complex

# 2. Explicit Type conversion

first_num = input('Enter first number: ')
second_num = input('Enter second number: ')
sum = first_num + second_num
print('Sum: ', sum)

first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
sum = first_num + second_num
print('Sum: ', sum)





