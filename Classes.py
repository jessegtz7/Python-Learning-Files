#a Class is like a blueprint for creating object. An object has properties and methods
#(functions) associates with it. Almost everything in Python is an object

#Creating a class
class Felino:
    #Contructor
    def __init__(self, especie, color, genero, edad):
        self.especie = especie
        self.color = color
        self.genero = genero
        self.edad = edad

    def informacion(self):
        return f'Soy un {self.especie} y soy de color {self.color} y tengo {self.edad} años.'

    def masEdad(self):
        self.edad += 1

#Extend a class
class Animales(Felino):
    #Constructor
    def __init__(self, especie, color, genero, edad):
        self.especie = especie
        self.color = color
        self.genero = genero
        self.edad = edad
        self.vidas = 0

    def set_vidas(self, vidas):
        self.vidas = vidas

    def informacion(self):
        return f'Soy un {self.especie} y soy de color {self.color} y tengo {self.edad} años y tengo {self.vidas} vidas.'

#Initialize User Object
ivan = Felino('Tigre', 'Werito', 'Macho', 10)
#Initicialize an Animal
melisa = Animales('Leon', 'Blanco', 'Hembra', 20)
melisa.set_vidas(7)
print(melisa.informacion())

ivan.masEdad()
print(ivan.informacion())