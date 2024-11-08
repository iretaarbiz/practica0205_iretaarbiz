'''Escribir una función que reciba una muestra de números en una lista y devuelva su media. '''
lista = list("12345")
def media(numeros):
    '''Función que recibe una muestra de números en una lista y devuelve su media. '''
    suma = 0
    for i in range(len(numeros)):
        suma += int(numeros[i])
    return suma / len(numeros)
print(media(lista))
