hola = "holaComoEstas"

def dx(hola):
    f = ""
    for i in hola:
            if i == i.upper():
                f += " "
            f += i     
    return f
print(dx(hola))