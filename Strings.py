name = 'Ivan'
age = 29

#Concateante
'''
print('His name is ' + name + ' and he is ' + age) -- this will result as a "TypeError: can only concatenate str (not "int") to str"
age mus be cast in to a str
'''
print('His name is ' + name + ' and he is ' + str(age))