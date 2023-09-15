# 14. Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los
# dos. En caso que sea letra, determine si es mayúscula o minúscula.
# Ingrese caracter: 9
# Es numero.
# Ingrese caracter: A
# Es letra mayúscula.
# Ingrese caracter: f
# Es letra minúscula.
# Ingrese caracter: #
# No es letra ni número.
caracter = input('Ingrese un caracter')
if caracter >= 'a' and caracter <= 'z':
    print('Es una letra minuscula')
elif caracter >= 'A' and caracter <= 'Z':
    print('Es una letra mayuscula')
elif caracter >= '0' and caracter <= '9':
    print('Es un numero')           
else : print('Es un simbolo')               