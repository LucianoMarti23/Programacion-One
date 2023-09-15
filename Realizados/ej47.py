# 47. Desarrolle un programa que calcule el dígito verificador de un código.
# Para calcular el dígito verificador, se deben realizar los siguiente pasos:
# 1. Obtener el código sin guion ni dígito verificador.
# 2. Invertir el número. (ej: de 201012341 a 143210102).
# 3. Multiplicar los dígitos por la secuencia 2, 3, 4, 5, 6, 7, si es que se acaban los números, se
# debe comenzar de nuevo, por ejemplo, con 143210102:
# 1×2+4×3+3×4+2×5+1×6+0×7+1×2+0×3+2×4=52
# 4. Al resultado obtenido, es decir, 52, debemos sacarle el módulo 11, es decir:
# 52 % 11 = 8
# 5. Con el resultado obtenido en el paso anterior, debemos restarlo de 11:
# 11 − 8 = 3
# 6. Finalmente, el dígito verificador será el obtenido en la resta de punto anterior, por lo cual el
# código con dígito verificador será: 201012341-3.

kdigo = int(input('\nIngrese el codigo: '))

def inversor_code(numero: int) -> int:
    return int(str(numero)[::-1])

def multiplicar_secuencia(numero: int) -> int:
    secuencia = [2, 3, 4, 5, 6, 7]
    secunciaMultiplicada: int = 0
    secuenciaIndice: int = 0
    for num in str(numero):
        secunciaMultiplicada = int(num) * secuencia[secuenciaIndice]
        if(secuenciaIndice == len(secuencia) - 1):
            secuenciaIndice = -1
        secuenciaIndice += 1 
    resultado: int = 11 - (secunciaMultiplicada % 11)
    return resultado if resultado > 0 else resultado * -1

print(f"El codigo verificador de {kdigo} es: {kdigo}-{multiplicar_secuencia(inversor_code(kdigo))}")


        




