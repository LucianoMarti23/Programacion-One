# 18. Hacer un algoritmo que permita ingresar un numero hasta el cual se mostrarán los números
# impares que le anteponían, ejemplo:
# usuario ingresa: 19
# algoritmo muestra: 1,3,5,7,9,11,13,15,17

num=int(input('Ingrese un numero: '))
for i in range(1,num,2): print(i)