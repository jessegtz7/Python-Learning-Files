# This is a single line comment.

'''
This a multipleline comment.
By using 3 single quotes
*(also used to define a functions purpose)
i can use a multiline comment section.
'''


"""
I can use Multiline
comments with double quotes to.
"""

# In all examples can be used to comment in the code.

"""
Variable Rules:
- Case sensitive... Azul and azul are different Variables
- Must star wiht a latter or an underscore: Printer, printer or _printer
- Can have numbers but can not start with one: 2Printer
- you can declare a variable without specifying if is INT, VAR o CHAR or STRING etc.
"""

# x = 10              #int
# Y = 2.1             #float
# Name = 'Jessus'     #str
# is_Red = True       #bool

#Multiple assignment
x, Y, Name, is_Red = (14, 3.6, 'Carlos', False)

#Basic Math
w = x + Y

print('Hi')
print(x, Y, Name, is_Red, w)

#Type and casting
print(type(x), type(Y), type(Name), type(is_Red), type(w))

w = str(w)
Y = int(Y)
Z = float(Y)
print(type(Z), Z, type(w), w)