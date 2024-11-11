'''Escribir una función que reciba una muestra de números 
en una lista y devuelva otra lista con sus valores al cuadrado'''

lista = list("12345")
def numeros_cuadrados(numeros):
    '''Función que recibe una muestra de números en una lista 
    y devuelve otra lista con sus valores al cuadrado'''
    for i in range(len(numeros)):
        numeros[i] = int(numeros[i]) ** 2
    return numeros
print(numeros_cuadrados(lista))
