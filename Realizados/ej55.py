# 55. Un analista financiero lleva un registro del precio del dólar día a día, y desea saber cuál fue la
# mayor de las alzas en el precio diario a lo largo de ese período.
# Escriba un programa que pida al usuario ingresar el número n de días, y luego el precio del dólar
# para cada uno de los n días.
# El programa debe entregar como salida cuál fue la mayor de las alzas de un día para el otro.
# Si en ningún día el precio subió, la salida debe decir: No hubo alzas.
# Cuantos dias? 10
# Dia 1: 96.96
# Dia 2: 99.03
# Dia 3: 96.03
# Dia 4: 93.27
# Dia 5: 88.82
# Dia 6: 92.16
# Dia 7: 90.32
# Dia 8: 90.67
# Dia 9: 90.89
# Dia 10: 94.10
# La mayor alza fue de 3.34 pesos




   
n = int(input("Ingrese la cantidad de dias : "))
precioDolar = []
for i in range(1,n+1):
    dolar=float(input("Ingrese el precio del dolar > "))
    precioDolar.append(dolar)


resta=[]
for d in range(1,len(precioDolar)):
    hola = precioDolar[d-1] - precioDolar[d]
    if hola<0:
        resta.append(hola)
print(min(resta))
print(resta)