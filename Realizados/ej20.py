# 20. Hacer un algoritmo que muestre la tabla de multiplicar de un numero ingresado por el usuario.
# Y que la muestre con el formato: A x B = C

table= int(input('Ingrese la tabla de quee numero quiere saber: '))
for i in range(1,11): print(f"{table} x {i} = {table*i}")