'''Escribir una función a la que se le pase una cadena <nombre>
 y muestre por pantalla el saludo ¡hola <nombre>!.'''
nombre = input("Escribe tu nombre: ")
def bienvenida(nombre):
    """"Funcion que muestra por pantalla el saludo ¡hola <nombre>!"""
    print('¡Hola', nombre, end="!")
    return
bienvenida(nombre)
