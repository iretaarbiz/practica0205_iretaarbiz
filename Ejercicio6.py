'''Escribir una función que convierta un número decimal en 
binario y otra que convierta un número binario en decimal'''
def binario_decimal(x):
    '''Esta función convierte un número decimal en 
    binario (recibe un numero entero) y devuelve una
    string con el numero binario'''
    binario = []
    aux = 0
    res = ""
    while x >= 1:
        aux = x
        x = x // 2
        resultado = aux % 2
        binario.append(resultado)
    binario.reverse()
    for i in range(len(binario)):
        res += str(binario[i])
    return res
print(binario_decimal(12))
def decimal_binario(y):
    '''Esta función convierte un número decimal en 
    binario (recibe un numero entero) y devuelve una
    string con el numero binario'''
    decimal = 0
    for i in range(len(y)):
        if y[i] == 1:
            decimal += 2 ** (len(y) - i)
    return decimal
print(decimal_binario(binario_decimal(12)))
