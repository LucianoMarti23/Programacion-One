texto = "Pig latin is cool"
hola = texto.split()




def pig_it(texto):

    
    return " ".join(list(map(lambda x : x[-1]+"ay" , texto.split())))

print(pig_it(texto))

hola = [0,4,1,2,3,0,0,0]

newlist=[]
contador = 0
for i in hola:
    if i != 0:
        newlist.insert(contador,i)
        contador+=1
        
    else  : newlist.append(i)

print(newlist)
