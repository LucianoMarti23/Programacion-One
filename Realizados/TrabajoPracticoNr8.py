# Crear un programa que le pida al usuario que ingrese un texto, lo que sea.
# Luego el programa le va a pedir al usuario que ingrese tres letras a su elección.
# Se procesará el texto para devolver:
# 1. Cuantas veces aparece cada letra que eligió el usuario, sin importar si aparecen en mayúsculas o
# minúsculas.
# 2. Cuantas palabras hay en el texto, y cuantas veces aparece cada una
# 3. Primera y última letra del texto.
# 4. Mostrar el texto invirtiendo el orden de las palabras.
# 5. Decir si determinada palabra ingresada por el usuario se encuentra en el texto.
# 6. Cuantas palabras hay de cada cantidad de letras (cuantas con una letra, cuantas con dos, cuantas
# con tres, etc.).

textoIngresado = input("Ingrese un texto u oracion : ")


textoIngresado = textoIngresado.lower()
print(textoIngresado)
x = textoIngresado.split()
Letras = []
for i in range(3):
    letraIngresada = input(f"Ingrese su {i+1} letra : ")
    Letras.append(letraIngresada)
             
aciertos = [h for h in (textoIngresado) if h in (Letras)]
for k in (Letras):
    print(f"La letra {k} se encuentra {aciertos.count(k)} veces en el texto")
                  
textoReversa = [orden for orden in reversed (x)]
s = " ".join(textoReversa)

conteoLetras = [len(q) for q in (x)]

repeticion = []
for repe in (conteoLetras):
    if repe not in repeticion:
        print(f"Las palabras con {repe} letras en total son {conteoLetras.count(repe)}")
        repeticion.append(repe)

cantidadPalabras = []
for i in (x):
    if i not in cantidadPalabras:
        print(f"La palabra {i} aparece :  {x.count(i)}  veces en el texto")
        cantidadPalabras.append(i)

print(f"El orden invertido de las palabras seria : {s}")
print(f"Hay {len(x)} palabras en el texto ingresado")
print(f"La primer letra es : {textoIngresado[:1]}\nLa ultima letra es : {textoIngresado[-1:]}")

usuario = input("Ingrese la palabra que quiera saber si se encuentra en el texto: ")
print(f"La palabra :{usuario}: Si  esta en el texto ") if usuario in (x) else print(F"la palabra :{usuario}: no esta en el texto")
            
#aparecen = dict()
#for word in (x):
    #aparecen[word] = aparecen.get(word,0) + 1        
        








#print(f"Las palabras repetidas  del texto aparecen con estos valores \n{aparecen}")        