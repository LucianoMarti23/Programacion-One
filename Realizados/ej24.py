# 24. Escriba un programa que pida al usuario la entrada correspondiente y calcule el factorial n! de
# un número entero n≥0, definido como:
# n!
# =1⋅2⋅3⋅⋯⋅n
# .
# Además, se define 0!=1

n = int(input('Ingrese el valor de n: '))
factorial=1
for i in range(n,0,-1):
    factorial*=i
        
print (f"El factorial de {n} ingresado es: {factorial}")    
   
