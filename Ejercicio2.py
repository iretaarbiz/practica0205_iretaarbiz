'''Escribir una función que reciba un número entero positivo y devuelva su factorial.
 Realiza el ejercicio mediante bucles interactivos y mediante una función recursiva.'''
def factorial_bucle(num):
    """Recibe un número entero positivo y devuelva su factorial mediante bucle for"""
    res = 1
    for i in range(1, num + 1):
        res = res * i
    return res
def factorial_recursivo(num):
    """Recibe un número entero positivo y devuelva su factorial mediante recursividad"""
    if num == 0:
        return 1
    else:
        return num * factorial_recursivo(num - 1)
print(factorial_bucle(5))
print(factorial_recursivo(5))
