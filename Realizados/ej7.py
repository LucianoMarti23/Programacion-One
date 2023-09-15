# 7. Una temperatura Celsius (centígrados) C puede ser convertida a una temperatura equivalente a
# F (Fahrenheit) de acuerdo a la siguiente formula:
# Escribir un programa que lea una temperatura de Celsius como número decimal y obtenga la
# temperatura Fahrenheit equivalente.

gradosCelsius=float(input('Ingrese una temperatura: '))
print('La temperatura en fahrenheit es ',(9/5) * gradosCelsius + 32)