def gcd(m,n):
    if n == 0:
        return m
    remainder = m%n
    if remainder == 0:
        return
    else:
        return gcd(n,remainder)
    
print(gcd(91,77))