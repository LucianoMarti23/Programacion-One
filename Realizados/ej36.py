# 36. Escriba un programa que entregue todos los divisores del número entero ingresado:
# Ingrese numero: 200
# # 1 2 4 5 8 10 20 25 40 50 100 200

numero = int(input('Ingrese un numero: '))

for i in range(1,numero+1,1):
    if (numero%i == 0):
        print(i,end = ' ')
        
        
       
           