# 51. En cada ronda del juego piedra, papel o tijera, los dos competidores deben elegir entre jugar
# tijera, papel o piedra.
# Las reglas para decidir quién gana la ronda son: tijera le gana a papel, papel le gana a piedra, piedra
# le gana a tijera, y todas las demás combinaciones son empates.
# El ganador del juego es el primero que gane tres rondas.

#  Escriba un programa que juegue con el usuario, muestre cuál es el marcador después de cada ronda,
#  y termine cuando uno haya ganado tres rondas. El jugador debe indicar su jugada escribiendo
#  tijera, papel o piedra. La computadora determina su jugada de formas aleatoria
import random




puntaje_usuario=0
puntaje_computador=0
while True:
 if puntaje_usuario == 3:
     print("El ganador es USUARIO!") 
     break
 elif puntaje_computador == 3:
     print("Computadora WINS")
     break          
 usuario = input("Piedra papel o tijera : ")
 usuario = usuario.lower()
 computador = random.choice(["piedra","papel","tijera"])
 if (usuario == "piedra" and computador == "tijera") or (usuario == "tijera" and computador == "papel") or (usuario == "papel" and computador == "piedra"):
        puntaje_usuario=puntaje_usuario+1
        print(f"Usuario : {usuario}\nComputador : {computador}\n {puntaje_usuario} - {puntaje_computador} ")
 elif (usuario == "piedra" and computador =="papel") or (usuario == "tijera" and computador == "piedra") or (usuario == "papel" and computador == "tijera"):
        puntaje_computador=puntaje_computador+1
        print(f"Usuario : {usuario}\nComputador : {computador}\n {puntaje_usuario} - {puntaje_computador}")
 else : print("Empate")              
       

           
    
    
               
     