'''Escribir una función que convierta un número decimal en 
binario y otra que convierta un número binario en decimal'''
def binario_decimal(x):
    '''Esta función convierte un número decimal en 
    binario (recibe un número entero) y devuelve una
    string con el número binario'''
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
def decimal_binario(y):
    '''Esta función convierte un número binario en 
    decimal (recibe un string) y devuelve un int
    con el número decimal'''
    decimal = 0
    for i in range(len(y)):
        if int(y[i]) == 1:
            decimal += 2 ** (len(y) - 1 - i)
    return decimal
print(binario_decimal(48))
print(decimal_binario("110000"))
print(binario_decimal(decimal_binario("110000")))
print(decimal_binario(binario_decimal(48)))

