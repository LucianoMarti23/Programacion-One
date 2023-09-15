# Trabajo práctico 2: Pirámide
# Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están
# construyendo una pirámide.
# Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide, es plana. La
# pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más
# que la capa superior.
# La figura ilustra la regla utilizada por los constructores:
# Su tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y
# generar la altura de la pirámide que se puede construir utilizando estos bloques.
# El programa debe devolver la altura de la pirámide y cuantos bloques sobraron.
# Nota: La altura se mide por el número de capas completas: si los constructores no tienen la
# cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo
# inmediatamente.
# Pruebe su código con los siguientes datos:
# Entrada de muestra: 6
# Salida esperada:
# La altura de la pirámide es: 3
# Sobraron: 0 piezas
# Entrada de muestra: 20
# Salida esperada:
# La altura de la pirámide es: 5
# Sobraron: 5 piezas
# Entrada de muestra: 1000
# Salida esperada:
# La altura de la pirámide es: 44
# Sobraron: 10 piezas
# Entrada de muestra: 2
# Salida esperada:
# La altura de la pirámide es: 1
# Sobraron: 1 piezas

#Nombre : Luciano Benjamin
#Apellido : Marti

n = int(input("Ingrese la cantidad de bloques : "))
altura = 0
bloquesTotal = n

for i in range(n,1,-1):
   if i >altura:
       altura = altura+1  
       bloquesTotal = bloquesTotal-altura
       if bloquesTotal <= altura:
           break
       
print(f"La altura de la piramide es : {altura}\nSobraron : {bloquesTotal} piezas ")       


    

