'''Escribir una función que calcule el área de un círculo y otra que 
calcule el volumen de un cilindro usando la primera función. '''

def area_circulo(radio):
    """Esta función calcula el area de un circulo, siendo el radio del circulo el parámetro de entrada"""
    return 3.14159 * (radio ** 2)
def volumen_cilindro(circulo, altura):
    """Esta función calcula el volumen de un cilindro, siendo el área del 
     circulo y la altura del cilindro los parámetros de entrada"""
    return area_circulo(circulo) * altura
print(volumen_cilindro(4, 3))