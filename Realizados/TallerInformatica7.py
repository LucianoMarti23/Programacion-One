def palindromos(n):
    c = ""
    for i in reversed(n):
        c  = c+i       
    if c == n:
        return True
    else : return False
         
print(palindromos("radar"))            