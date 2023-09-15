import subprocess


word = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"


proceso  =  subprocess.call([word])

if proceso == 0:

    print("Comando Ejecutado Satisfactoriamente.")

else:

    print("Comando Fallido el retorno es de : ", proceso)

    
