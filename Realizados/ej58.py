# 58. Escribir un programa que pregunte el correo electrónico del usuario y lo valide (debe tener @).

while True:
    n = input("Ingrese tu correo electronico > ")
    if "@" in n:
        break
    else : print('Correo incorrecto , debe tener > @')

print("Correo correcto")






