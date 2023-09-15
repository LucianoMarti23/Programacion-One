# 8. Un sistema de ecuaciones lineales
# ax + by= e
# dx + ey= f
# Se puede resolver con las siguientes formulas:
# Diseñar un programa que lea dos conjuntos de coeficientes (a, b, c; d, e y f) y visualice los valores
# de X y Y

a = int(input('Ingrese el valor de A: ')) #Conjunto 1
b = int(input('Ingrese el valor de B: '))
c = int(input('Ingrese el valor de C: '))
x = 0
d = int(input('Ingrese el valor de D: '))#Conjunto 2
e = int(input('Ingrese el valor de E: '))
f = int(input('Ingrese el valor de F: '))
y = 0
if (c*e-b*f) >0 and (a*e-b*d) >0: 
 x= (c*e-b*f)/(a*e-b*d)
 y= (a*f-c*d)/(a*e-b*d)
 
print(f"El valor de X es{x} y el valor de Y es {y}")