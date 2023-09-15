# 40. Escriba un programa que entregue la suma de los primeros n números naturales, siendo n
# ingresado por el usuario.
# Matemáticamente lo que se pide que haga el programa es realizar la siguiente sumatoria.
# S1=1+2+3+4+5+6+⋯+n
# Además, obtenga el resultado de la siguiente fórmula.
# S2=n×(n+1)/2
# El programa debe entregar el resultado diciendo si S1 y S2 son iguales o no.
n =int( input('Ingrese el numero n: '))
s1 = 0
s2=(n*1)*(n+1)/2
for i in range(1,n+1,):
    s1 += i
if s1 == s2 :   
 print(f"S1 y S2 son iguales {s1} y {s2}")
else: print(f"No son iguales, {s1} y {s2}")     