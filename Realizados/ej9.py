# 9. Escribir un programa para convertir una medida dada en pies a sus equivalentes en: a) yardas;
# b) pulgadas; c) centímetros, y d) metros (1 pie = 12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54
# centímetros, 1 metro = 100 centímetros). Leer el numero de pies e imprimir el número de yardas,
# pies, pulgadas, centímetros y metros.
datePie= float(input('Ingrese el numero de pies: '))
pulgada= (datePie*12)
yarda = (datePie/3)
centimetro = (datePie*30.48)
metro = (datePie*0.3048)
print('La medida dada en pies son',pulgada,'en pulgadas')
print(f"La medida dada en pies son {yarda:.4f} en yardas")
print('La medida dada en pies son',centimetro,'en centimetros')
print('La medida dada en pies son',metro,'en metros')

