#A Dictionary is a collection which is unordered, cangeable and indexed. No Duplicate members.

#Create a dictionary
laptop = {
    'Marca': 'Lenovo',
    'Modelo': 'T470',
    'HDD': 250
}

print(laptop, type(laptop))

#use constructor
laptop2 = dict(marca='Apple', modelo='MacBook Pro', HDD=500)

print(laptop2, type(laptop2))

#Get a Value/Key
print(laptop['Modelo'])
print(laptop.get('HDD'))

#Add Value/Key
laptop['RAM'] = '8GB'
print(laptop)

#Get dictionaries values/Key
print(laptop.keys())

#Get dictionaries Items
print(laptop.items())

#Copy Dictionary
laptop3 = laptop.copy()
laptop3['Procesador'] = 'Intel'
print(laptop3)

#Remove item
del(laptop['Modelo'])
laptop.pop('Marca')
print(laptop)

#Clear
laptop3.clear()
print(laptop3)

#get lenght
print(laptop2)
print(len(laptop2))

#List of dictionaries
impresoras = [
    {'Marca': 'Xerox', 'Cartucho': 'Toner'},
    {'Marca': 'HP', 'Cartucho': 'Tinta'}
]

print(impresoras)
print(impresoras[1]['Cartucho'])