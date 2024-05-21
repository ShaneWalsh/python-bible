# Python Variables # case sensitive
# Numbers
    # dynamiclly typed, you change the type of variable by reassigning it.
    # type(number) to get variable type
    # 'int' 'float' 'str'
    # Number operators (+ - * / %)
    # Division always returns a float. 16bytes
    # BODMAS Ordering to Math operations.

    # Casting type int(floatvalue)

    # imports at the top of the file, duh.
    # import math # trig functions cos/sin/tan take radians not degrees.
    # pandas, NumPy, SciPy are good maths modules

num = 1
print(num + 1)

num += 5
print(num + num)

num2 = (num+1) + 100
print(num2)

print(num2 < 100)
print(num2 < 100 | num2 > 105)
num3 = 99
print((num2 > 100 & num2 < 105) | num3 < 100)

str1 = "Sample"

print(str1,num3)

print(num2 == 100)
print(num2 >= 100)
print('float ' + str(num2 / 3))
print('is float', type(num2 / 3) == float)
print('is float', type(num2 * 3) == float)
print('mod', num2 % 7)

# Strings
print('hello world')
print(' he said "hello world i can\'t" ')
overlineVariable = ''' first line
second line '''
print(overlineVariable)

