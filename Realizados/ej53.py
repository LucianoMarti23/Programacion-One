# 53. Los números de Fibonacci Fk son una sucesión de números naturales definidos de la siguiente
# manera:
# F0F1Fk=0,=1,=Fk−1+Fk−2,cuando k≥2.
# En palabras simples, la sucesión de Fibonacci comienza con 0 y 1, y los siguientes términos siempre
# son la suma de los dos anteriores.
# En la siguiente tabla, podemos ver los números de Fibonacci desde el 0-ésimo hasta el duodécimo.



# # a. Escriba un programa que reciba como entrada un número entero n, y entregue como salida el
# # n-ésimo número de Fibonacci:
# # Ingrese n: 11
# # F11 = 89
# # b. Escriba un programa que reciba como entrada un número entero e indique si es o no un
# # número de Fibonacci:
# # Ingrese un numero: 34
# # 34 es numero de Fibonacci
# # Ingrese un numero: 78
# # 78 no es numero de Fibonacci
# # c. Escriba un programa que muestre los m primeros números de Fibonacci, donde m es un
# # número ingresado por el usuario:
# # Ingrese m: 7
# # Los 7 primeros numeros de Fibonacci son:
# # 0 1 1 2 3 5 8
# #



b = int(input("Ingrese N : "))
def fib(n):
    if n < 2:
        return n
    else:
        
        return fib(n-1) + fib(n-2)
print(fib(b))

d = int(input("Saber si es o no num fibonacci : "))
x = 0
y = 1
z = 0

while True:  
    z=x+y
    x = y
    y = z
    if d == z:
        print(f"Es un numero fibonacci : {d}")
        break
    elif z > d:
        print("No es numero fibonacci")
        break
    
m = int(input("Hasta que numeros queres imprimir?:  "))    
for x in range(m):
    print(fib(x))

   
    
    
        
        
                     