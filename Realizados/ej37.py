# 37. Desarrolle un programa para estimar el valor de π usando la siguiente suma infinita:
# π=4*(1−1/3+1/5−1/7+…)
# La entrada del programa debe ser un número entero n que indique cuántos términos de la suma se
# utilizará.
# n: 3
# 3.466666666666667
# n: 1000
# 3.140592653839794


n1=int(input('Ingrese un entero: '))
def numero_n(n):
    numero = ((-1)**n)/((2*n)+1)
    return numero
pi = 0 
for i in range(0,n1):
      pi= pi+numero_n(i)
print(f"La sumatoria es {pi*4}")


       