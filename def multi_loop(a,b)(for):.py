def multi_loop(a,b):
    result = 0
    if b>0:
        for i in range(1,b+1):
            result +=a
    return result
print(multi_loop(3,5))
