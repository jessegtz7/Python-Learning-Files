name = 'Ivan'
age = 29

#**Concateante**
'''
print('His name is ' + name + ' and he is ' + age) -- this will result as a "TypeError: can only concatenate str (not "int") to str"
age mus be cast in to a str
'''
print('His name is ' + name + ' and he is ' + str(age))

#**String format**

#1.- Arguments by position.
print('His name is {nombre} and he is {edad}'.format(nombre=name, edad=age))

#2.- F-Strings (On Python 3.6+)
print(f'His name is {name} and he is {age}')

#**String methods**
g = 'blue printer'
print(g)

#Capitalize string
print(g.capitalize())

#All Uppercase
print(g.upper())

#All Lower
print(g.lower())

#Swap case
print(g.swapcase())

#Get length
print(len(g))

#Replace
print(g.replace('blue', 'orange'))

#Count
sub = 'p'
print(g.count(sub))

#Starts with
print(g.startswith('printer'))

#Ends with
print(g.endswith('r'))

#Split into a last
print(g.split())

#Find position
print(g.find('e'))

#Is all alphanumeric
print(g.isalpha())

#Is all numeric
print(g.isnumeric())

#Look for the outputs