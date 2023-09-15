def fibo (n:int):
    if n == 1 or n == 0:
        return 1
    return fibo(n-1)+ fibo(n-2)
    
for i in range(10):
    print(fibo(i))    