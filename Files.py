#Python has functions for creating, reading, updating and deleting files.

#Open a file
miArchivo = open('ejemploArchivo.txt', 'w')

#Get some info
print('Name: ', miArchivo.name)
print('is Closed: ', miArchivo.closed)
print('Opening Mode: ', miArchivo.mode)

#Write to file
miArchivo.write('I love Ivan')
miArchivo.write(' and he is my brother')
miArchivo.close()

#Append to file
miArchivo = open('ejemploArchivo.txt', 'a')
miArchivo.write('. Love you brother.')
miArchivo.close()

#Read form a File
miArchivo = open('ejemploArchivo.txt', 'r+')
texto = miArchivo.read(50)
print(texto)