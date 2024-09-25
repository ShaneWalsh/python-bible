# Python Variables # case sensitive
# Numbers
    # dynamiclly typed, you change the type of variable by reassigning it.
    # type(number) to get variable type
        # 'int' 'float' 'str' 'bool'
    # Number operators (+ - * / %)
    # Division always returns a float. 16bytes
    # BODMAS Ordering to Math operations.

    # Casting type int(floatvalue)

    # imports at the top of the file, duh.
    # import math # trig functions cos/sin/tan take radians not degrees.
    # pandas, NumPy, SciPy are good maths modules

# Python Standard Lib in the docs does not need to be imported, they are OOTB.

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
# String methods are functions specific to stirngs.
# Immutable
print('hello world')
print(' he said "hello world i can\'t" ')
overlineVariable = ''' first line {} pop
second line '''
print(overlineVariable.format('Snap'))
template= "Whoooo {1}, you are soooo {0}"
output = template.format(8,'Shane')
print(output)
print(len(output))
print(output.count("Shane"))
print(output.lower())
print(output.upper())
print(output.isupper())
print(output.istitle())
print("1234".isdigit())
print(output.isalpha()) # contains a space
print(output.isalnum()) # only letters or numbers
print(output.index("are")) # value error if not found, no -1
print(output.find("ara")) # returns -1 if no index

print(output.strip("W")) # lstrip rstrip, trim on certain characters. Empty input, Defualt is spaces

# str Slice (substring) (start,end,stepsize) upto but not including
print("slice",output[0:8:1])
print("slice in steps of 2",output[0::2])
print("slice from 5",output[5:])
print("slice reverse",output[::-1])
print("slice negative string value",output.strip()[-6]) # position from the end.


## Booleans, comparisons (<,>,==,!=,>=,<=), logic (not,same as ! in java, and, or)
truthy = True != False
print(type(truthy), truthy)
d = 5

if truthy:
    print('must be true')
elif truthy != True:
    print('must not be true')
else:
    print('must be unknown!')

if not truthy:
    print('must be false')

if (d > 3 and d < 10 and d != 0) or d != 5:
    print("and/or is working")



## List - Array []
our_list = [27,46,-5]
print(our_list)
type(our_list)

mixed = ["A","B","C",[1,2,3],"C",True,"Absolute madness"]
print(mixed[0]+"_"+mixed[1])
print(mixed[0:4]) # Slice for a new array with the same values. e.g obj references

messy = mixed[0:4]
messy[3][1] = 4 # This is a change to an Obj, that both lists ref, so ti changes in both.
print(messy)
print(mixed)
print(len(mixed))

del mixed[4] # drop the extra C!
print(mixed)

mixed = mixed + [2] # add to the end of the array
mixed = mixed + [[2,2]] # add [] as an element.
mixed = mixed + list("BCD") # will add all 3 individualy to the list.
mixed = mixed + list(str(123)) # will add all 3 individualy to the list.
print(mixed)

# insert at position.
mixed.insert(1,100); # 1 is index, 100 is the value.
mixed.append(2) # return type is none NoneType
mixed.remove(1)

# List Comprehension
# newlist = [expression for item in iterable if condition == True]
amazing = [x for x in range(1,11) if x%2==0 ]
print("Comprehension :", amazing )


## Tuple - Final ()
# Similar to a list, but its immutable.
my_tuple = (1,2,3,"4","D")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0:2])
a = [1,2,3]
print(tuple(a))
D,E,F = [1,2,3]


## Dictionaries - Map {}
# no ordering, no indexing, just key value pairs.
students = {"jim":25,"ann":31}
print(students["jim"])

students["shane"] = 32
students["shane"] = 33
print(students)

del students["jim"]
print(students)

keys = list(students.keys())
values = list(students.values())
print(keys)

print("All students are {}".format(" ".join(list(students.keys()))))

# Tuple of each key value pairing.
items = list(students.items())
print(items)






#
