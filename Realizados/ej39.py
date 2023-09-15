# 39. Escriba un programa que muestre los números naturales menores o iguales que un número n
# determinado, que no sean múltiplos ni de 3 ni de 7.
# Ingrese numero: 24
# 12458
# 10
# 11
# 13
# 16
# 17
# 19
# 20
# 22
# 23

n = int(input('Ingrese un numero: '))
acumulador = [] 
#acumulador = [i for i in range(1, n + 1) if (i % 3 != 0 and i % 7 != 0)]
for i in range(1,n,1):
   if i % 3 == 0 or i % 7 == 0  or (i%3 !=0 and i%7 ==0) or (i%3 == 0 and i%7 !=0):
       continue
   else: acumulador.append(i)
                  
print(acumulador)             

  
         