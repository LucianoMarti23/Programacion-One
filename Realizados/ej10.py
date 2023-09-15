# 10. La relación entre los lados (a, b) de un triángulo rectángulo y la hipotenusa (h) viene dada por
# la fórmula.
# a2 + b2 = c2
# Escribir un programa que lea la longitud de los lados y calcule la hipotenusa.
import math


ladoA=int(input('Ingrese la longitud de lado A:' ))
ladoB=int(input('Ingrese la longitud lado B:' ))
proceso=(ladoA**2+ladoB**2)
hipotenusa= math.sqrt(proceso)
print('La logintud de lado A es: ',ladoA, 'y la longitud de lado b es: ',ladoB,'y su hipotenusa es: ',hipotenusa,)

