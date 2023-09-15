# 22. Hacer un algoritmo que permita ingresar N números y que luego calcule la suma y el promedio
# de los números ingresados.
condition = True
nums = []
while condition:
    num=int(input("Ingrese un numero: "))
    nums.append(num)
    confirmacion =int(input('Desea continuar?\nIngrese 0 si quiere terminar\nOtro cualquier numero para continuar: '))
    if confirmacion == 0:
        condition = False

print(f"EL promedio de {nums} es {sum(nums)/len(nums)}")