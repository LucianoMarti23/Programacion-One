# 31. Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada
# uno de los lados no puede ser más largo que la suma de los otros dos.
# Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:
# si acaso el triángulo es inválido; y
# si no lo es, qué tipo de triángulo es.
ladoA= float(input('Ingrese a: '))
ladoB= float(input('Ingrese b: '))
ladoC= float(input('Ingrese c: '))
if (ladoA + ladoB)<ladoC or (ladoB+ladoC)<ladoA or (ladoA + ladoC)<ladoB:
    print('No es un triangulo valido')
elif (ladoA + ladoB)>ladoC or (ladoB + ladoC)>ladoA or (ladoA + ladoC)>ladoB:
    if  (ladoA == ladoB == ladoC):
        print('Es un triangulo Equilatero')
    elif (ladoA==ladoB != ladoC or ladoA==ladoC != ladoB or ladoB==ladoC !=ladoA):
        print('Es un triangulo Isosceles')
    else : print('Es un triangulo Escaleno')
           