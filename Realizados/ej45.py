# 45. Desarrolle un programa que permita determinar la cantidad total de puntos que contiene un
# juego de dominó de 28 piezas.
# A modo de ejemplo, considere la pieza de la siguiente figura, la cual tiene 7 puntos.
# Además, recuerde que en el dominó cada lado de una pieza toma valores entre 0 y 6 y que, por
# ejemplo, la pieza cuyos lados toman valores 1 y 4 es la misma que la pieza con valores 4 y 1.


acumulador = 0
iterador = 0
for i in range(0,8):
    for j in range(0,7):
     acumulador+= j     
    iterador +=1
print(acumulador)                