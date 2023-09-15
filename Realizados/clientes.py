from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
raiz = Tk()
raiz.title("Turnos Medicos")
raiz.geometry("800x600")

idCLiente = StringVar()

nombreCliente = StringVar()

apellidoCliente = StringVar()

edad = StringVar()

correoElectronico = StringVar()

direccionCliente = StringVar()

numeroCliente = StringVar()



def conexionBBDD():
    miConexion = sqlite3.connect("base")
    miCursor= miConexion.cursor()

    try :
        miCursor.execute('''
        CREATE TABLE  cliente (
        ID INTEGER PRIMARY KEY AUTOINCREMENT
        NOMBRE VARCHAR(30)
        APELLIDO VARCHAR(30)
        EDAD INT(10)
        CORREO VARCHAR(50)
        DIRECCION VARCHAR(40)
        NUMEROCLIENTE INT(20))
        ''')
        messagebox.showinfo("CONEXION, BASE DE DATOS CREADA CORRECTAMENTE ")
    except :     
            messagebox.showinfo("CONEXION", "EXITOSA con la base de datos")

def salirAplicacion():
     valor = messagebox.askquestion ("Salir","Estas seguro que desea salir de la aplicacion")
     if valor == "yes":
          raiz.destroy()

def limpiarCampos():
     nombreCliente.set("")
     apellidoCliente.set("")
     edad.set("")
     correoElectronico.set("")
     direccionCliente.set("")
     numeroCliente.set("")


def crear():
    miConexion = sqlite3.connect("base")
    miCursor = miConexion.cursor()
    try : 
         datos = nombreCliente.get(),apellidoCliente.get(),edad.get(),correoElectronico.get(),direccionCliente.get(),numeroCliente.get()
         miCursor.execute(" INSER INTO empleado VALUES (NULL,?,?,?,?,?,?)",(datos))
         miConexion.commit()
    except :
         messagebox.showinfo("ADVERTENCIA","OCURRIO UN ERROR AL CREAR EL REGISTRO")
         limpiarCampos()


def mostrar():
     miConexion = sqlite3.connect("base")
     miCursor = miConexion.cursor()
     registros = tree.get_children()
     for elemento in registros:
          tree.delete(elemento)

     try : 
          miCursor.execute("SELECT * FROM cliente ")
          for row in miCursor:
               tree.insert("",0,text=row[0] , values = (row[1], row[2] , row[3]))
     except : 
          pass

tree = ttk.Treeview(height=10,columns=('#0','#1','#2','#3'))
tree.place(x=0,y=140)     
tree.column('#0',width=100)
tree.heading('#0',text="ID",anchor=CENTER)
tree.heading('#1',text="NOMBRE",anchor=CENTER)
tree.heading('#2',text="DIRECCION",anchor=CENTER)
tree.heading('#3', text="CORREO",anchor=CENTER)
tree.column('#3', width=100)



def actualizar():
     miConexion = sqlite3.connect("base")
     micursor = miConexion.cursor()
     try:
          datos = nombreCliente.get(),apellidoCliente.get(),edad.get(),correoElectronico.get(),direccionCliente.get(),numeroCliente.get()
          micursor.execute("UPDATE cliente SET NOMBRE=? , APELLIDO=? , EDAD=? , CORREO= ? , DIRECCION=? , NUMEROCLIENTE= ? WHERE ID="+idCliente.get(),(datos))
          miConexion.commit()
     except :
          messagebox.showwarning("ADVERTENCIA" , "OCURRIO UN ERROR AL ACTUALIZAR EL REGISTRO")
          pass
     limpiarCampos()
     mostrar()

def borrar():
     miConexion = sqlite3.connect("base")
     miCursor = miConexion.cursor()
     try:
          if messagebox.askyesno(message="Realmente desea eliminar el registro?", title="ADVERTENCIA"):
               miCursor.execute("DELETE FROM cliente WHERE ID ="+idCLiente.get())
     except : 
                messagebox.showwarning("ADVERTENCIA" , "OCURRIO UN ERROR AL BORRAR EL REGISTRO")
                pass
                limpiarCampos()
                mostrar()


menubar = Menu(raiz)

menubasedat = Menu(menubar,tearoff=0)

menubasedat.add_command(label="Crear/Conectar Base de Datos" , command=conexionBBDD)
menubasedat.add_command(label="Salir Aplicacion",command=salirAplicacion)
menubar.add_cascade(label="Inicio" , menu=menubasedat)


ayudaMenu = Menu(menubar,tearoff=0)

ayudaMenu.add_command(label="Limpiar Campos" , command=limpiarCampos)
menubar.add_cascade(label="Herramientas",menu=ayudaMenu)


e1 =Entry(raiz, textvariable=idCLiente)


l2 = Label(raiz, text="Nombre")
l2.place( x=50 , y=10)


e2 = Entry(raiz, textvariable=nombreCliente , width=10)

e2.place(x=100 , y=10)

l3 = Label(raiz, text="Apellido")
l3.place( x=50 , y=40)


e3 = Entry(raiz, textvariable=apellidoCliente , width=10)

e3.place(x=100 , y=40)

l4 = Label(raiz, text="Edad")
l4.place( x=50 , y=70)


e4 = Entry(raiz, textvariable=edad , width=10)

e4.place(x=100 , y=70)


l5 = Label(raiz, text="Correo")
l5.place( x=50 , y=100)


e5 = Entry(raiz, textvariable=correoElectronico , width=20)

e5.place(x=100 , y=100)


l6 = Label(raiz, text="Direccion")
l6.place( x=200 , y=40)


e6 = Entry(raiz, textvariable=direccionCliente , width=20)

e6.place(x=260 , y=40)


l7 = Label(raiz, text="Telefono")
l7.place( x=200 , y=10)


e7 = Entry(raiz, textvariable=numeroCliente , width=10)

e7.place(x=260 , y=10)


b1 = Button(raiz,text="Crear Registro" , command=crear)
b1.place(x=0, y=380)

b2 = Button(raiz,text="Modificar Registro" , command=actualizar)
b2.place(x=100 , y=380)

b3 = Button(raiz,text=" Lista Pacientes" , command=mostrar)
b3.place(x=220 , y=380)

b4= Button(raiz,text="Eliminar Registro",  command=borrar)
b4.place(x=320, y=380)
raiz.config(menu=menubar)



raiz.mainloop()