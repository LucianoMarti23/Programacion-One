# 23. Hacer un algoritmo que analice si en dos números ingresados: cual es mayor, cual es menor, o si
# son iguales.
numone=int(input('Ingrese el primer num: '))
numTwo=int(input('Ingrese el segundo num: '))
print(f"{numone} es mayor a {numTwo}") if numone > numTwo else print(f"{numTwo} es mayor a {numone}") if numTwo>numone else print("Son iguales")
