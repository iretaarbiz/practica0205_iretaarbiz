'''Escribir una función que convierta un número decimal en 
binario y otra que convierta un número binario en decimal'''
def binario_decimal(num):
    binario = []
    aux = 0
    resultado = "Hola"
    while num >= 1:
        aux = num
        num = num // 2
        resultado = aux % 2
        binario.append(resultado)
    for i in range(len(binario), 0, -1):
        return resultado + str(binario[i-1])
print(binario_decimal(64))