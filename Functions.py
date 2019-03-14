#A function is a block of code which only runs when it is called. Indentation with tabs or spaces are used instead of {}.

#Create function
def todayIs(dia):
    print(f'Hoy es {dia}.')

todayIs('Jueves')

#Another way to call a function
def helloThere(nombre='Ivan'):
    print(f'Hola {nombre}.')

helloThere()

#Retunr Values
def getRes(n1, n2):
    totalr = n1 - n2
    return totalr

print(getRes(10, 8))

#Other way
def getSum(n3, n4):
    totals = n3 + n4
    return totals

num = getSum(5, 10)
print(num)

#Other way
'''
def getMul(n5, n6):
    return n5 * n6

num1 = int(input())
num2 = int(input())
mult = getMul(num1,num2)
print(mult)
'''

#Lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.

def getDiv(n7, n8):
    return n7 / n8

getDiv = lambda n7, n8 : n7 / n8

print(getDiv(12, 4))