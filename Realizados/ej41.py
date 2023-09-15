# 41. Escriba un programa que permita determinar el número mayor perteneciente a un conjunto de n
# números, donde tanto el valor de n como el de los números deben ser ingresados por el usuario.
# Ingrese n: 4
# Ingrese número: 23
# Ingrese número: -34
# Ingrese número: 0
# Ingrese número: 1
# El mayor es 23
n = int(input('Ingrese el valor de n  : '))
t = set()

for i in range(1,n+1):
    adicion = int(input('Ingrese un numero: '))
    t.add(adicion)
            
print(f"El numero mayor es {max(t)} y todo los valores del conjunto son {t}")        
    
    