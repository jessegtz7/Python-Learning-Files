#If/Else conditions are used to decide to do something based on something being true or false

a = 20
b = 8

#Comparison Operator (==, !=, >, <, >=, <=) - Used to copare values

#Simple if
if a > b:
    print(f'{a} is greater than {b}.')

#If/else
if a < b:
    print(f'{a} is greater than {b}.')
else:
    print(f'{a} is not greater than {b}.')

#elif
c = 30
d = 30

if c > d:
    print(f'{c} ir greater than {d}.')
elif c == d:
    print(f'{c} is equal to {d}.')
else:
    print(f'{c} is not greater than {d}')

#Nested if
if a > 10:
    if a <= 20:
        print(f'{a} is greater than 10 and less than or equal to 20.')

#Logical operator (and, or, not) - Used to combine conditional statements
#and: both have to be true
if b > 5 and b <= 20:
    print(f'{b} is greater than 5 and less than or equal to 20.')

#or: one or the other have to be true
if c < 21 or c < 50:
    print(f'{c} is greater than 21 or less than 50.')

#not
if not(a == c):
    print(f'{a} is not equals to {c}')


#Membership Operators (in, not in) - Membership to operators are used to test if a sequence is presented in an object

numbers = [4, 8, 12, 16, 20]

#not
if b in numbers:
    print(b in numbers)

#not in
if c not in numbers:
    print(c not in numbers)


#Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

#is
if c is d:
    print(c is d)

#is not
if a is not b:
    print(a is not b)