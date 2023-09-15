# 16. Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:
#     Por supuesto, el resultado entregado depende del día en que su programa será ejecutado.
# Para obtener la fecha actual, puede hacerlo usando la función localtime que viene en el módulo
# time. Los valores se obtienen de la siguiente manera (suponiendo que hoy es 11 de marzo de 2020)
# El programa debe tener en cuenta si el cumpleaños ingresado ya pasó durante este año, o si todavía
# no ocurre.
from time import localtime
t= localtime()
dayActually=t.tm_mday
mondayActually=t.tm_mon
yearActually=t.tm_year
year=int(input('Ingrese el anio que naciste '))
monday=int(input('Ingrese el mes que naciste'))
day=int(input('Ingrese el dia que naciste'))
print("Feliz",yearActually-year,"Anios") if yearActually>=year and mondayActually==monday and dayActually==day else print("Usted tiene: ",yearActually-year-1,"Anios, Todavia no cumplio anios") if yearActually>=year and mondayActually<=monday and day>0 else print("Utedd tiene",yearActually-year,"Anios, Usted Ya cumplio anios ") if yearActually>=year and mondayActually>=monday and day>0 else print("nothing")

          
    

