# 25. Un alumno desea saber que nota necesita en el tercer parcial para aprobar. El promedio se
# calcula con la siguiente formula.
# NP=(P1+P2+P3)/3
# NF=NP⋅0.7+NL⋅0.3
# Donde NP es el promedio de parciales, NL el promedio de prácticos y NF la nota final.
# Escriba un programa que pregunte al usuario las notas de los dos primeros parciales y la nota
# promedio de prácticos, y muestre la nota que necesita el alumno para aprobar la materia con nota
# final 60.
# Ingrese nota parcial 1: 45
# Ingrese nota parcial 2: 55
# Ingrese nota prácticos: 65
#  Necesita nota 72 en el parcial 3

p1=int(input('Ingrese la nota del primer parcial: '))
p2=int(input('Ingrese la nota del segundo parcial: '))
tp=int(input('Ingrese el promedio de TPs: '))
p3=((60-tp*0.3)/0.7)*3-p1-p2
print(f"Debe sacar {int(p3)} en el 3er parcial ")