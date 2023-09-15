
a = 0
while a == 0:
    try:
        a = int(input("Ingrese el valor de a: "))
        if(a == 0):
            print("\nIngrese un valor distinto a 0.\n")
    except:
        print("\nError - Ingrese un numero entero mayor a 0.\n")
  
while True:
    try:
        b = int(input("Ingrese el valor de b: "))
        c = int(input("Ingrese el valor de c: "))
        break
    except:
        print("\nError - Ingrese numeros enteros\n")
    

discriminante = b**2 - 4 * a * c
mensaje = ""
if(discriminante < 0):
    mensaje = "La ecuacion no tiene soluciones reales."
elif(discriminante == 0):
    x = -b / (2 * a)
    mensaje = f"La unica solucion real es: {x}"
else:
    r1 = (-b + discriminante**0.5) / (2*a)
    r2 = (-b - discriminante**0.5) / (2*a)
    mensaje = f"La raiz1 es {r1} y la raiz2 es {r2}."

print(f"\nLa ecuacion {a}x2 + {b}x + {c} \nTiene las siguientes raices: {mensaje}\n")