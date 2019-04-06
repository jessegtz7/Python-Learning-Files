#a for Loop is used for iterate over a sequence (that is either a list, tuple, dictionary, set or string).

empresas = ['IBM', 'DELL', 'HP', 'INTEL']

#Simple for loop
for posiblesTrabajos in empresas:
    print(f'Posibles puestos en: {posiblesTrabajos}')
print('***Simple Loop***')


#Break that stops when the condition is found
for posiblesTrabajos2 in empresas:
    if posiblesTrabajos2 == 'HP':
        break
    print(f'Posibles puestos en: {posiblesTrabajos2}')
print('***Loop and Break***')

#Continue
for posiblesTrabajos3 in empresas:
    if posiblesTrabajos3 == 'IBM':
        continue
    print(f'Posibles puestos en: {posiblesTrabajos3}')
print('***Loop and Continue***')

#Range
for i in range(0, 5):
    print(f'Numeros: {i}')
print('***loop and Range***')

#While Loops: execute a set of statements as long as a conditions is true
conteo = 0
while conteo <= 5:
    print(f'Numeros: {conteo}')
    conteo += 1
print('***loops and while***')