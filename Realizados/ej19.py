# 19. Hacer un algoritmo que haga lo siguiente:
# Pida dos números al usuario, y que los multiplique. Si la multiplicación da un valor menor a 150, se
# volverán a pedir los números hasta que la multiplicación de ambos tengan una respuesta mayor a
# 150. Mostrar la respuesta en cada intento.


result=0
while result<150:
    numOne=int(input('\nIngrese el primer num: '))
    numTwo=int(input('Ingrese el segundo numero: '))
    result=numOne*numTwo
    print(result)
    
