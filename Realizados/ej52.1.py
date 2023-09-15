import random
mayor = 100
menor = 0
intentos = 0
while True:
 intentos = intentos+1
 r = random.randint(menor,mayor)
 print(r)
 respuesta = input("Es mayor o menor o igual?: ")
 if respuesta == '<':
    mayor = r
 elif respuesta == '>':
     menor = r
 elif respuesta == '=': 
     print (f"Adivinaste en {intentos}") 
     break
        
        
     

     
     
 
                 
 
         