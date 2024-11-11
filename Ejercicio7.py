x = int(input("Introduce el numero en decimal: \n"))
binario = []
aux = 0
while x >= 1:
    aux = x
    x = x // 2
    resultado = aux % 2
    binario.append(resultado)
    binario.reverse()
print(binario)
for i in range(len(binario), 0, -1):
    print(binario[i-1], end="")