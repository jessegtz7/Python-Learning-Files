#Tuple is a collection which is in order and unchangeable. Allows duplicate members.**

#Create a tuple
colors = ('Azul', 'Rojo', 'Amarillo')

#Contructor -- another way to create tuple. Not very common but use full
colors2 = tuple(('Azul', 'Rojo', 'Amarillo'))

print(colors, colors2)

#Single value needs trailing comma
colors2 = ('Azul',)

#Get value
print(colors[1])

print(colors2, type(colors2))

#Can't Change Value
#Uncoment this to see the output - colors[0] = 'Naranja'

#Leng
print(len(colors))

#Delete tuple
'''
del colors2
print(colors2)
'''

#**A Set is a collection which is unsorted and unindexed. No duplicate members.**

#Create a set
cars_set = {'Vocho', 'Camioneta', 'Van', 'Combi'}
print(cars_set)

#Check if in set
print('Camioneta' in cars_set)

#Add to Set
cars_set.add('Pecero')
print(cars_set)

#Remove from set
cars_set.remove('Combi')
print(cars_set)

#Add duplicate
cars_set.add('Vocho')
print(cars_set)

#Clear set
cars_set.clear()
print(cars_set)

#Delete
del cars_set
print(cars_set)