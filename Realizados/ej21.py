# 21. Hacer un algoritmo que pida 10 números y luego indique cuantos fueron pares y cuantos
# impares
numsTotales=[]
for i in range(1,11): 
 num=int(input(f"Ingrese el {i}° numero: "))
 numsTotales.append(i)   
pares = list(filter(lambda x : x % 2 == 0,numsTotales))
impares = list(filter(lambda y : y % 2 != 0,numsTotales))
print(f"Los numeros Impares fueron : {impares} y los numeros pares fueron {pares}")  