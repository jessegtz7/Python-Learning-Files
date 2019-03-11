#A List is a collections which is ordered and changeable. allows Duplicate Members.

#Create a List
numbers = [1, 2, 3, 4, 5]
animals = ['Vacas', 'Perros', 'Gallinas', 'Gatos']

#Contructor -- another way to create list. Not very common but use full
numbers2 = list((1, 2, 3, 4, 5))
print(numbers, numbers2)

#Get a Value -- 0 is the base for the list. In "Vacas" is 0, "Perros" 1, etc
print(animals[1])

#Get length
print(len(animals))

#Append to list
animals.append('Ratones')
print(animals)

#Remove from list
animals.remove('Gallinas')
print(animals)

#Intert into position
animals.insert(2, 'Cotorros')
print(animals)

#Remove with pop
animals.pop(3)
print(animals)

#Reverse list
animals.reverse()
print(animals)

#Sort list
animals.sort()
print(animals)

#Reverse Sort
animals.sort(reverse=True)
# animals.reverse()
print(animals)

#Change Value
animals[0] = 'Caballos'
print(animals)