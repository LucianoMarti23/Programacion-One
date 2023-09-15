# 42. Escriba un programa que muestre todas las combinaciones posibles al momento de lanzar dos
# dados de 6 caras:
acumulador =0
iterador = 1

while iterador<7:
 for j in range(1,7):
         acumulador+=1
         print(iterador,acumulador)
        
 acumulador =0         
 iterador+=1
 print('---')         