# 48. Un tablero de ajedrez es una grilla de 8 × 8 casillas. Cada celda puede ser representada
# mediante las coordenadas de su fila y su columna, numeradas desde 1 hasta 8.
# El caballo es una pieza que se desplaza en forma de L: su movimiento consiste en avanzar dos
# casillas en una dirección y luego una casilla en una dirección perpendicular a la primera:

# Escriba un programa que reciba como entrada las coordenadas en que se encuentra un caballo, y
# entregue como salida todas las casillas hacia las cuales el caballo puede desplazarse.
# Todas las coordenadas mostradas deben estar dentro del tablero.
# Si la coordenada ingresada por el usuario es inválida, el programa debe indicarlo.
# Ingrese coordenadas del caballo.
# Fila: 2
# Columna: 8
# El caballo puede saltar de 2 8 a:
# 1 6
# 3 6
# 4 7
# Ingrese coordenadas del caballo.
# Fila: 3
# Columna: 4
# El caballo puede saltar de 3 4 a:



# a = int(input("Ingrese la fila del caballo : "))
# b = int(input("Ingrese la columna del caballo: "))

# def movimiento_invalido (a:int,b:int):
#     if (a<1 or a >8) or (b<1 or b >8):
#         return print('Movimiento invalido')  
# movimiento_invalido(a,b) 
                
# def movimiento_validos(a:int,b:int):         
#  if(a >=3 and a <=6) and (b >=3 and b <=6):
#   return print(f"Los posibles saltos son : {a+2,b-1} , {a+2,b+1} {a+1,b-2} , {a-1,b-2} , {a+1,b+2} , {a-1,b+2} , {a-2,b-1} y {a-2,b+1}")
#  elif (a <3 and b<6) or (a<3 and b>6):
#      if a == 2 and b == 2:
#        return  print(f"Los unicos movimientos posibles son : {a+2,b-1} , {a+2,b+1} , {a+1,b+2} y {a-1,b+2}")
#      elif (a == 2 and b == 3) or (a == 2 and b == 4) or (a == 2 and b == 5) or (a == 2 and b == 6):
#        return print(f"Los movimientos posibles son :{a+2,b-1} {a+2,b+1} {a+1,b-2} {a+1,b+2} , {a-1,b-2} y {a-1,b+2} ")   
#      elif a == 2 and b == 1:
#          return print(f"Los unicos movimientos posibles son : {a+2,b+1} , {a+1,b+2} y {a-1,b+2}")
#      elif a == 2 and b == 7:
#          return print(f"Los unicos movimientos posibles son : {a+2,b-1} , {a+2,b+1} , {a+1,b-2} y {a-1,b-2}")
#      elif a == 2 and b == 8:
#          return print(f"Los unicos movimientos posibles son : {a+2,b-1} , {a+1,b-2} y {a-1,b-2}")
#      elif a == 1 and b == 2:
#          return print(f"Los unicos movimientos posibles son : {a+2,b-1} , {a+2,b+1} y {a+1,b+2}")
#      elif (a == 1 and b == 3) or (a == 1 and b == 4) or (a == 1 and b == 5) or (a == 1 and b == 6):
#          return print(f"Los movimienntos posibles son : {a+2,b-1} , {a+2,b+1} , {a+1,b-2} y {a+1,b+2} ")
#      elif a == 1 and b == 1 :
#          return print(f"Los unicos movimientos posibles son {a+2,b+1} y {a+1,b+2}")
#      elif a == 1 and b == 8 :
#          return print(f"Los unicos movimientos posibles son :{a+2,b-1} y {a+1,b-2} ")
#      elif a == 1 and b == 7:
#          return print(f"Los unicos movimientos posibles son :{a+2,b-1} , {a+2,b+1} , {a+1,b-2} ")    
#  elif (a == 3 and b == 2) or (a == 4 and b == 2) or (a == 5 and b == 2) or (a == 6 and b == 2):
#      return print(f"Los unicos movimientos posibles son {a+2,b-1} , {a+2,b+1} ,{a+1,b+2} , {a-1,b+2}, {a-2,b+1} y {a-2,b-1}")
#  elif (a == 3 and b == 1) or (a == 4 and b == 1) or (a == 5 and b == 1) or (a == 6 and b == 1) :
#      return print(f"Los unicos movimientos posibles son : {a+2,b+1} ,{a+1,b+2} , {a-1,b+2} y {a-2,b+1} ")         
#  elif (a == 3 and b == 7) or (a == 4 and b == 7) or (a == 5 and b == 7) or (a == 6 and b == 7):         
#       return print(f"Los unicos movimientos posibles son : {a+2,b-1} , {a+2,b+1} , {a+1,b-2}, {a-1,b-2} ,{a-2,b-1} y {a-2,b+1}")
#  elif (a == 3 and b == 8) or (a == 4 and b == 8) or (a == 5 and b == 8) or (a == 6 and b == 8):
#      return print(f"Los saltos posibles son : {a+2,b-1} , {a+1,b-2} , {a-1,b-2} y {a-2,b-1} ")
#  elif (a == 8 and b == 1):
#      return print(f"Los movimienntos posibles son {a-1,b+2} y {a-2,b+1}")
#  elif (a == 8 and b == 2):
#     return  print(f"Los unicos movimientos posibles son: {a-1,b+2} , {a-2,b-1} y {a-2,b+1}")
#  elif (a == 8 and b == 3) or (a == 8 and b == 4) or (a == 8 and b == 5) or (a == 8 and b == 6):
#      return print(f"Los movimenntos posibles son : {a-1,b-2} , {a-1,b+2} {a-2,b+1} y {a-2,b-1}")
#  elif (a == 8 and b == 7):
#      return print(f"Los movimienntos posibles son : {a-1,b-2} , {a-2,b-1} y {a-2,b+1}")
#  elif (a == 8 and b == 8):
#      return print(f"Los movimientos posibles del caballo son :{a-2,b-1} y {a-1,b-2} ")
#  elif (a == 7 and b == 1):
#      return print(f"Los movimientos posibles son : {+1,b+2} , {a-1,b+2} y {a-2,b+1} ")
#  elif (a == 7 and b == 2 ):
#      return print(f"Los movimientos posibles son : {a+1,b+2} , {a-1,b+2} , {a-2,b-1} y {a-2,b+1}")
#  elif (a == 7 and b == 3 ) or (a == 7 and b == 4) or (a == 7 and b == 5) or (a == 7 and b == 6):
#      return print(f"Los movimientos posibles son : {a+1,b-2} , {a+1,b+2} , {a-1,b-2} , {a-1,b+2} , {a-2,b-1} y {a-2,b+1} ")
#  elif (a == 7 and b == 7 ):
#      return print(f"Los movimientos posibles son : {a+1,b-2} , {a-1,b-2} , {a-2,b-1} y {a-2,b+1}")
#  elif (a == 7 and b == 8):
#      return print(f"Los movimientos posibles son : {a+1,b-2} , {a-1,b-2} y {a-2,b-1}")
# movimiento_validos(a,b)

# a = int (input("Ingrese la fila del caballo en que se encuentra : "))
# b = int(input("Ingrese la columna del caballo en que se encuentra : "))
# if (a >=1 and b >=1)  and (a<= 8 and b <=8):
#  if (a+2 >=1 and b-1 >=1) and (a+2 <=8 and b-1 <=8 ):
#         print(a+2,b-1)
#  if (a+2 >=1 and b+1 >=1 ) and (a+2 <=8 and b+1 <=8):
#         print(a+2,b+1)
#  if (a+1 >=1 and b-2 >=1) and (a+1 <=8 and b-2 <=8):
#          print(a+1,b-2)
#  if (a-1  >=1 and b-2 >=1) and (a-1  <=8 and b-2 <=8 ):
#          print(a-1,b-2)
#  if (a+1 >=1 and b+2 >=1) and (a+1 <=8 and b+2 <=8):
#          print(a+1,b+2)
#  if (a-1 >=1 and b+2 >=1) and (a-1 <=8 and b+2 <=8):
#          print(a-1,b+2)
#  if (a-2 >=1 and b-1 >=1) and (a-2  <=8 and b-1 <=8):
#          print(a-2,b-1)
#  if (a-2 >=1 and b+1 >=1) and (a-2 <=8 and b+1 <=8):
#          print(a-2,b+1)
# else : print("Movimiento invalido") 


a = int(input("Ingrese la fila  : "))
b = int(input("Ingres la columna :  "))

def movimientosCaballo(a,b):
 dic = [(a+2,b-1),(a+2,b+1),(a-2,b-1),(a-2,b+1),(a-1,b-2),(a-1,b+2),(a+1,b-2),(a+1,b+2)]
 if a <=0 or b <=0 or a>8 or b>8:
    return print("Movimiento invalido")
 for h,j in dic:
    if h  >=1 and j >=1  and h<=8 and j <=8:
         print(f"El caballo puede moverse a {h,j}")
        
movimientosCaballo(a,b)         

 


                    
   
                       
        
        
   
   
    

     

        
    