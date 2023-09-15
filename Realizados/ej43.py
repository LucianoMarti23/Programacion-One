# 43. Un jugador debe lanzar dos dados numerados de 1 a 6, y su puntaje es la suma de los valores
# obtenidos.
# Un puntaje dado puede ser obtenido con varias combinaciones posibles. Por ejemplo, el puntaje 4 se
# logra con las siguientes tres combinaciones: 1+3, 2+2 y 3+1.
# Escriba un programa que pregunte al usuario un puntaje, y muestre como resultado la cantidad de
# combinaciones de dados con las que se puede obtener ese puntaje.

# Ingrese el puntaje: 4
# Hay 3 combinaciones para obtener 4
# Ingrese el puntaje: 11
# Hay 2 combinaciones para obtener 11
# Ingrese el puntaje: 17
# Hay 0 combinaciones para obtener 17


acumulador =0
iterador = 1
n = int(input('Ingrese un el puntaje: '))
combinaciones = 0
while iterador<7:
 for j in range(1,7):
         acumulador+=1
         if (iterador + acumulador) == n:
             combinaciones +=1
        
 acumulador =0         
 iterador+=1
 
print(f"Hay {combinaciones} combinaciones para obtener {n}") 