# 49. Un número natural es un palíndromo si se lee igual de izquierda a derecha y de derecha a
# izquierda (capicúa). Por ejemplo, 14941 es un palíndromo, mientras que 81924 no lo es.
# Escriba un programa que indique si el número ingresado es o no palíndromo:
# Ingrese un numero: 14941
# 14941 es palindromo
# Ingrese un numero: 81924
# 81924 no es palindromo

numero = (input('Ingrese un numero : '))
print("Es capicua") if numero == numero[::-1] else print("No es capicua")       
    
  
