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
del colors2
print(colors2)


#**A Set is a collection which is unsorted and unindexed. No duplicate members.**

