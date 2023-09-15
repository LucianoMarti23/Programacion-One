# 50. Así como hay números palíndromos, también hay palabras palíndromas, que son las que no
# cambian al invertir el orden de sus letras.
# Por ejemplo, «reconocer», «Neuquén» y «acurruca» son palíndromos.
# 1. Escriba un programa que reciba como entrada una palabra e indique si es palíndromo o no.
# Para simplificar, suponga que la palabra no tiene acentos y todas sus letras son minúsculas:
# Ingrese palabra: sometemos
# Es palindromo
# Ingrese palabra: rascar
# No es palindromo


palabra = input('Ingrese su palabra: ')
palabra=palabra.lower()

if palabra == palabra[::-1]:
    print(f"Es palindromo la palabra {palabra}")
else : print(f"No es palindromo la palabra {palabra}")


oracion = input("Ingrese la oracion : ")
oracionn = oracion.lower()


if oracion.replace(" ","") == oracion.replace(" ","")[::-1]:
    print(f"La oracion : {oracion} , es palindromo")
else : print(f"La oracion : {oracion} , no es palindromo ")        