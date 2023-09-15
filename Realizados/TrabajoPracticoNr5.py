# # Trabajo práctico 5: Ta-Te-Ti
# # Su tarea es escribir un simple programa que simule jugar a ta-te-ti con el usuario. Para hacerlo
# # más fácil, Hemos decidido simplificar el juego. Aquí están nuestras reglas:
# # • La maquina jugará utilizando las 'X's.
# # • El usuario jugará utilizando las 'O's.
# # • El primer movimiento es de la maquina: siempre coloca una 'X' en una posición al azar.
# # • Todos los cuadros están numerados comenzando con el 1 (observe el ejemplo para que tenga
# # una referencia).
# # • El usuario ingresa su movimiento introduciendo el numero de cuadro elegido. El numero
# # debe de ser valido, un valor entero entre 1 y 9, y no puede ser un cuadro que ya esté
# # ocupado por una X o un O.
# # • El programa verifica si el juego ha terminado. Existen cuatro posibles veredictos: el juego
# # continua, el juego termina en empate, gana el usuario, o la maquina gana.
# # • La maquina responde con su movimiento y se verifica el estado del juego.
# # • Opcionalmente puede implementar algún tipo de inteligencia artificial, o la maquina elegirá
# # un cuadro de manera aleatoria.
# # -
# Nombre : Luciano Benjamin
# Apellido : Marti
import random
b =  ("""         ╦───╦───╦───╦ 
         │ 1 │ 2 │ 3 │
         ╬───╬───╬───╬
         │ 4 │ 5 │ 6 │
         ╬───╬───╬───╬
         │ 7 │ 8 │ 9 │
         ╚───╩───╩───╝""")
#No modificar la variable "b"
#Porque cambiara los indices de los numeros

while True:
  numero  = chr(random.randint(ord('1'), ord('9')))
  if numero  in (b): 
   b = b.replace(numero,'X')
   print(f"La computadora juega el movimiento : {numero}\n{b}")
   
   if (b[35] == 'X' and  b[81] == 'X' and b[127] == 'X')\
    or(b[39] == 'X' and b[85] == 'X' and b[131] == 'X')\
    or(b[43] == 'X' and b[89] == 'X' and b[135] == 'X')\
    or(b[35] == 'X' and b[39] == 'X' and b[43] == 'X')\
    or(b[81] == 'X' and b[85] == 'X' and b[89] == 'X')\
    or(b[127] == 'X' and b[131] == 'X' and b[135] == 'X')\
    or(b[35] == 'X' and b[85] == 'X' and b[135] == 'X')\
    or(b[43] == 'X' and b[85] == 'X' and b[127] == 'X'):
    print("La Computadora Gano")
    print(b)
    break
   if("1" not in b) and ("2" not in b)\
    and ("3" not in b) and ("4" not in b)\
    and ("5" not in b) and ("6" not in b)\
    and ("7" not in b) and ("8" not in b) and ("9" not in b):
     print("Empate")
     print(b)
     break  
   usuario = input("Ingrese su movimiento : ")
   if usuario not in b:
     while True :
       print("El movimiento que usted eligio ya esta ocupado")
       usuario = input("Ingrese su movimiento : ")
       if usuario in b :
         break
   b = b.replace(usuario,'O') 
   if (b[35] == 'O' and  b[81] == 'O' and b[127] == 'O')\
   or (b[39] == 'O' and b[85] == 'O' and b[131] == 'O')\
   or (b[43] == 'O' and b[89] == 'O' and b[135] == 'O')\
   or(b[35] == 'O' and b[39] == 'O' and b[43] == 'O')\
   or(b[81] == 'O' and b[85] == 'O' and b[89] == 'O')\
   or(b[127] == 'O' and b[131] == 'O' and b[135] == 'O')\
   or(b[35] == 'O' and b[85] == 'O' and b[135] == 'O')\
   or(b[43] == 'O' and b[85] == 'O' and b[127] == 'O'):
    print(b)
    print("Has Ganado!")
    break
     
# combinacion1 = "1,4,7..-35,81,127"
# combinacion2 = "2,5,8...-39,85,131"
# conmbinacion3 = "3,6,9...-43,89,135"
# combinacion4 = "1,2,3...-35,39,43"
# combinacion5 =  "4,5,6...-81,85,89"
# combinacion6 =  "7,8,9..-127,131,135"
# combinacion7 = "1,5,9..-35,85,135"
# combinacion8 = "3,5,7..-43,85,127" 



