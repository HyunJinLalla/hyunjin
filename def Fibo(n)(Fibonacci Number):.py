def Fibo(n):
    if n<1:
        return 0
    elif n ==1:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)
    
print(Fibo(18))