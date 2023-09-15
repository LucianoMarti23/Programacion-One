# # Trabajo práctico 4: Contraseña
# # Crear un generador de contraseñas aleatorias en Python que deben
# # cumplir los siguientes requisitos:
# # • Entre 10 y 15 caracteres
# # • Al menos una letra mayúscula
# # • Al menos una letra minúscula
# # • Al menos cuatro números, no consecutivos ni repetidos
# # • Al menos un carácter no alfanumérico, por ejemplo: #!@] *($

#Nombre : Luciano Benjamin
#Apellido : Marti

import random
nums = ['0','1','2','3','4','5','6','7','8','9']
letrasMin = "abcdefghijklmnopqrstuvwxyz"
letrasMay = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
simbolos = "#$%^&*()"


d = set()

while len(d)<4:
    d.add(random.choice(nums))
    
    
d = list(d)

    
while len(d)<13:
    d.append(random.choice(letrasMin))
    d.append(random.choice(letrasMay))
    d.append(random.choice(simbolos))

condition = True

while condition: 
    random.shuffle(d)
    for i in range(len(d)):
        if d[i-1] in nums and d[i] in nums:
            print(d)
            break
    for h in range(len(d)):
        print(d)
        if d[i-1] not in nums and d[i] not in nums:
         condition = False
                       
contraGenerada = "".join(d)

print(f"La password generada es : {contraGenerada}") 
 
         
      
     
 

         
         
   





   