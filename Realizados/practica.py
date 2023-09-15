
valoresDegradado = {"bolsa de plastico":150,
                    "botella de pet":1000,
                    "envases de tetrabik":30,
                    "chicle":5}

eleccion = input("elegir uno de los siguientes elementos\n1=Bolsa de plastico\n2-Botella de peta\n3-Envases de tetrabik\n4-Chicle  \nIngrese su material : ").lower()


def valoresTrue(eleccion):
    return valoresDegradado[eleccion]

if  eleccion in valoresDegradado.keys():
    print(f"El degradado del material es de {valoresTrue(eleccion)} anios") 
          
else : print("El material no se encuentra en las opciones dadas")          