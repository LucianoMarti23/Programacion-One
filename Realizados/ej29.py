# 29. Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más
# larga y por cuántas letras lo es.
# Palabra 1: edificio
# Palabra 2: tren
# La palabra edificio tiene 4 letras mas que tren.
# Palabra 1: sol
# Palabra 2: paralelepipedo
# La palabra paralelepipedo tiene 11 letras mas que sol
# Palabra 1: plancha
# Palabra 2: lapices
# Las dos palabras tienen el mismo largo
a = (input('Ingrese la primer palabra:'))
b = (input('Ingrese la segunda palabra:'))
print(f"La palabra mas larga es {a}") if len(a)>len(b) else print(f"La palabra mas larga es {b}")