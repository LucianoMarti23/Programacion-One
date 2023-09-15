def procedimiento(n:list):
    iterador = ""
    for i in (n):
        print(iterador)
        iterador = ""
        for j in range(i):
            iterador = iterador+"*"        
    return iterador

n = [5,10,20]

print(procedimiento(n))        
        