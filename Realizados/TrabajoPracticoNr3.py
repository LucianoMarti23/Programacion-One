

# Nombre : Luciano Benjamin
# # Trabajo práctico 3: Primos
# # Un número natural es primo si es mayor que 1 y no tiene divisores más que 1 y si mismo.
# # ¿Complicado? De ninguna manera. Por ejemplo, 8 no es un número primo, ya que puede dividirlo
# # entre 2 y 4 (no podemos usar divisores iguales a 1 y 8, ya que la definición lo prohíbe).
# # Por otra parte, 7 es un número primo, ya que no podemos encontrar ningún divisor para él que no
# # sean 1 y 7. Su tarea es escribir una función que verifique si un número es primo o no.
# # La función:
# # • Se llama esPrimo.
# # • Toma un argumento (el valor a verificar).
# # • Devuelve True si el argumento es un número primo, y False de lo contrario.
# # Para probar la función, realizar un programa que muestre los número primos menores o iguales a
# # uno ingresado por el usuario.

#Nombre : Luciano Benjamin
#Apellido : Marti

primo = int(input("Ingrese un numero : "))

def esPrimo(n):
     for i in range(2,n):
         if (n%i) == 0:
             return False
     return True    

primos = []
for i in range(primo,1,-1):
    if esPrimo(i):
        primos.append(i)
          
print(primos)










        