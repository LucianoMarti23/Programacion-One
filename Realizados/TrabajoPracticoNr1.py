# Trabajo práctico 1: Calculadora de impuesto
# En un municipio la gente paga varios impuestos. El impuesto más importante, denominado
# Impuesto Personal de Ingresos (IPI, para abreviar) tiene que pagarse
# una vez al año y se evalúa utilizando la siguiente regla:
# • Si el ingreso del ciudadano no es superior a 85.718 pesos, el
# impuesto es igual al 18% del ingreso menos 596 pesos y 2
# centavos (esta fue la llamada exención fiscal ).
# • Si el ingreso es superior a esta cantidad, el impuesto es igual
# a 14,319 pesos y 2 centavos, más el 32% del excedente sobre
# 85.718 pesos.
# Su tarea es escribir una calculadora de impuestos.
# • Debe aceptar un valor de punto flotante: el ingreso del ciudadano.
# • A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales (sin
# centavos).
# Nota: Este municipio nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado es
# menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero). Tenga esto
# en cuenta durante sus cálculos.
# El código solo lee un valor de entrada y genera un resultado.
# Pruebe su código con los datos siguientes
# Entrada de muestra: 10000
# Resultado esperado: El impuesto es: 1204.0 pesos
# Entrada de muestra: 100000
# Resultado esperado: El impuesto es: 18889.0 pesos
# Entrada de muestra: 1000
# Resultado esperado: El impuesto es: 0.0 pesos
# Entrada de muestra: -100
# Resultado esperado: El impuesto es: 0.0 pesos

#Nombre : Luciano Benjamin
#Apellido : Marti


ingreso = float(input("Ingresos : "))
excedente = (ingreso-85718)
impuestoInferior = (18 * ingreso /100) - 596.2
impuestoSuperior = 14319.2 + (32*excedente/100)
if ingreso <=85718 and impuestoInferior>0:
 print(f"El impuesto es de : {round(impuestoInferior):.1f} pesos ")
elif ingreso > 85718 and impuestoSuperior>0 :
 print(f"El impuesto es de : {round(impuestoSuperior):.1f} pesos ")
else : print("El impuesto es 0.0 pesos")




 

