# Trabajo práctico 7: Ahorcado
# Juego de adivinanza El Ahorcado, en el que el jugador tiene que adivinar las letras para encontrar
# una palabra oculta. La versión más básica del juego no tiene que incluir gráficos, puedes hacerlo un
# proyecto basado en texto.
# En primer lugar, necesitará una lista de palabras para el sistema para elegir una al azar (se puede
# cargar de un archivo o generarla de un texto). Después, tendrá que elegir las funciones apropiadas
# para revisar si la entrada del usuario es una letra, si la palabra oculta la contiene, y si es así, cuántas
# veces. Su código también tendrá que usar la función print para mostrar las letras encontradas o no, y
# limitar el número de intentos.
import random 

palabras = ["pelota",
            "estadio",
            "futbol",
            "jugadores",
            "arbitro",
            "arco",
            "lesion",
            "goles",
            "asistencia",
            "expulsion",
            "suplentes",
            "titulares",
            "corner",
            "tirolibre",
            "sustitucion",
            "comentarista",
            "entrenador",
            "penal",
            "canilleras",
            "cesped",
            "botines",
            
            
            
            ]
d = """"          ╦════╦  
           1    ║
          324   ║  
          5 6   ║
                ║ 
               ═╩═
                 """
#cord.-31 "O",
#cord.-49 "│",
#cord.-48 "<",
#cord.-50 ">",
#cord.-68 "┘",
#cord.-70 "└" 

palabraOculta = random.choice(palabras)
palabra = palabraOculta
for i in (palabraOculta):
 palabra = palabra.replace(i,"-")


s = ""
l = list(palabra)
intentos = 0
print(d)
print(palabra)
while True:
 if palabraOculta == s:
             print(f"Has Ganado!\n{d}\nCon {6-intentos} intentos disponibles!")
             break       
 letra = input("Ingrese una letra : ")
 i = list(palabra)
 if len(letra)>1:
     print("Error!: Has ingresado mas de una letra")
     continue 
 if letra in (palabraOculta):
     for i in range(len(palabraOculta)):
         if palabraOculta[i] == letra:
             l[i] = letra
             s = "".join(l)
 print(d)                
 print(f"La letra {letra}\nAparece {palabraOculta.count(letra)} veces")         
 print(s)                
 if letra not in (palabraOculta):
     intentos +=1
     print(f"Letra equivocada, te quedan {6-intentos} intentos")
     if intentos == 1:
      d = d.replace(str(intentos),"O")
      print(f"{d}\n{s}")
     elif intentos == 2 :
         d = d.replace(str(intentos),"│")
         print(f"{d}\n{s}") 
     elif intentos == 3 :
         d = d.replace(str(intentos),"<")
         print(f"{d}\n{s}") 
     elif intentos == 4 :
         d = d.replace(str(intentos),">")
         print(f"{d}\n{s}") 
     elif intentos == 5 :
         d = d.replace(str(intentos),"┘")
         print(f"{d}\n{s}") 
     elif intentos == 6 :
         d = d.replace(str(intentos),"└")
         print(f"{d}\n{s}\nHas Perdido!\nLa palabra era {palabraOculta}")                 
         break     
   