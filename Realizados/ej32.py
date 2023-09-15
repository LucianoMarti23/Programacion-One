# 32. El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de
# masa corporal:
# edad < 45 edad ≥ 45
# IMC < 22.0 bajo medio
# IMC ≥ 22.0 medio alto
# El índice de masa corporal (IMC) es el cociente entre el peso del individuo en kilos y el cuadrado
# de su estatura en metros.
# Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le
# entregue su condición de riesgo.
estatura = float(input('Ingrese su estatura: '))
peso = int(input('Ingrese su peso: '))
edad = int(input('Ingrese su edad: '))
imc = peso/(estatura**2)

if edad <45:
  if imc<22.0:
      print(f"tu indice de masa corporal es: {imc} y tu riesgo es : Bajo")
  elif imc>=22.0:
      print(f"tu indice de masa corporal es: {imc} y tu riesgo es : Medio")
elif edad>=45:
    if imc<22.0:
        print(f"tu indice de masa corporal es : {imc} y tu riesgo es : Medio ")
    elif imc>=22.0:
        print(f"tu indice de masa corporal es : {imc} y tu riesgo es : Alto")                              