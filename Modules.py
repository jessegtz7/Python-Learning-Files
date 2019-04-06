#a Module is a file containing a set of functions to include your aplication
#There are core python modules, modules you can install using the pip package
#manager (including Django) as well as custom modules.
#Core Modules
import datetime
from datetime import date
import time
from time import time

#pip Module
from  camelcase import CamelCase

#Date & Time
hoy = datetime.date.today()
print(hoy)

hoy2 = date.today()
print(hoy2)

    #hora = time.time()
    #print(hora)

hora2 = time()
print (hora2)

#CamelCase uppercase exercise
a = CamelCase()
print(a.hump('hola mundo'))


#Custom Module *Check the Validator.py file*
import Validator
from Validator import validar_correo

email = 'prueba@prueba.com'
print(email)
if validar_correo(email):
    print('El correo es valido')
else:
    print('El correo no es valido')

email2 = 'prueba#prueba.com'
print(email2)
if validar_correo(email2):
    print('El correo es valido')
else:
    print('El correo no es valido')