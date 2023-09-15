#  Lotería Chaqueña le encarga realizar un simulador para un nuevo juego que lanzará próximamente.
#  Es una variación de la Quiniela Poceada existente.
#  Modalidad
#  Se trata de un juego poceado. Para definir el extracto del juego, se tomarán al azar 20 (veinte)
#  números de dos cifras (del 00 al 99).
#  Cada apostador deberá confeccionar su boleta eligiendo 8 (ocho) números de dos dígitos, distintos
#  entre si, del 00 al 99.
#  Si los números elegidos están dentro de los 20 números del extracto del sorteo, sin importar el
#  orden, obtendrá un premio.
#  Ganará un premio de la Poceada quien acierte 8, 7, 6 ó 5 números. Por lo cual se necesita saber
#  cuantos ganadores acertaron con cada cantidad de aciertos.
#  Se necesita realizar un programa que simule los sorteos.
#  Primeramente se deben generar al azar una cantidad n de boletas.
#  Luego realizar el sorteo de los 20 números (seleccionados al azar).
#  Y por último realizar los cálculos de resultados (cuantas boletas hubo con 8, 7, 6 ó 5 aciertos)

import random


sorteado = []
while len(sorteado)<20:
    d = random.randrange(0,99)
    if d not in (sorteado):
        sorteado.append(d)


n = int(input("Ingrese la cantidad de boletas : "))

boletas = []

for i in range(n):
    boletas.append([])
    while len(boletas[i])<8:
     c = random.randrange(0,99)
     if c not in (boletas):
       boletas[i].append(c)

boletaganadora = []         
aciertoss = 0       
for aciertos in (boletas):
    if aciertoss >=5:
        boletaganadora.append(aciertoss)
    aciertoss = 0    
    for cantidadaciertos in (aciertos):
        if cantidadaciertos in (sorteado):
            aciertoss +=1
boletaganadora.append(aciertoss)            
             
print(f"Los numeros sorteados fueron {sorteado}")
print(f"Boletas con 8 aciertos fueron:  {boletaganadora.count(8)}\nBoletas con 7 aciertos fueron:  {boletaganadora.count(7)}")
print(f"Boletas con 6 aciertos fueron:  {boletaganadora.count(6)}\nBoletas con 5 aciertos fueron:  {boletaganadora.count(5)}")
print(f"Las boletas elegidas fueron {boletas}")


                         