import sqlite3


miConexion = sqlite3.connect("Base")
miCursor = miConexion.cursor()


# miCursor.execute('''
#                  CREATE TABLE PRODUCTOS (
#                      CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
#                      NOMBRE_ARTICULO VARCHAR(50),
#                      PRECIO INTEGER,
#                      SECCION VARCHAR(20))
#                  ''')

# objetos = [("AR01" , "Pelota" , 15 , "Jugueteria"),
#              ("AR02" , "Raqueta", 20 , "Jugueteria"),
#              ("AR03" , "Camiseta",100 , "Deportes"),
#              ("AR04" , "Mouse"   , 150 , "Electronica"),
#              ]


miCursor.execute("INSERT INTO PRODUCTOS VALUES() ")

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)",objetos)









miConexion.commit()






miConexion.close()

