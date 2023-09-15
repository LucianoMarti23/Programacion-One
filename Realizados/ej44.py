# 44. Desarrolle un programa que tenga la siguiente entrada:
#  primero, el usuario ingresa un número entero n, que indica cuántas palabras ingresará a
# continuación;
#  después el usuario ingresa n palabras.
# La salida del programa debe mostrar la palabra más larga y la más corta que fueron ingresadas por
# el usuario.
# Recuerde que la función len entrega el largo de un string:
# len('amarillo') -> 8
# La ejecución del programa debe verse así:
# Cantidad de palabras: 5
# Palabra 1: negro
# Palabra 2: amarillo
# Palabra 3: naranjo
# Palabra 4: azul
# Palabra 5: blanco
# La palabra mas larga es amarillo
# La palabra mas corta es azul

n = int(input('La cantidad de palabra es : '))
palabras = []
for i in range(1,n+1):
    j = input('Ingrese las palabras: ')
    palabras.append(j)

[print(f"Palabra {index+1}: {item}") for index, item in enumerate(palabras)]      
print(f"La palabra mas larga es {max(palabras, key=len)}")
print(f"La palabra mas corta es {min(palabras, key=len)}")

  
# def findLongestWordInAlist(list):
#     maxWord = list[0]
#     maxWords = []
#     for item in list:
#         if(len(item) == len(maxWord)):
#             maxWords.append(item)
#         elif(len(item) > len(maxWord)):
#             maxWord = item
#     if(len(maxWords) > 0 and len(maxWords[0]) < len(maxWord)):
#         maxWords.pop(0)
#     return maxWords if len(maxWords) > 1 else maxWord

# def findShorterWordInAlist(list):
#     minWord = list[0]
#     minWords = []
#     for item in list:
#         if(len(item) < len(minWord)):
#             minWord = item
#         elif(len(item) == len(minWord)):
#             minWords.append(item)
#     if(len(minWords) > 0 and len(minWords[0]) > len(minWord)):
#         minWords.pop(0)
#     return minWords if len(minWords) > 1 else minWord

# def printListElements(list):
#     for index, item in enumerate(list):
#         print(f"Palabra {index+1}: {item}")  

# print(printListElements(palabras))    
# print(f"La palabra mas larga es: {findLongestWordInAlist(palabras)}")
# print(f"La palabra mas corta es: {findShorterWordInAlist(palabras)}")
        