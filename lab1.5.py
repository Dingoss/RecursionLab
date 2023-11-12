def Pow(x, n):
    if n == 0:
        return 1.0

    if n < 0:
        x = 1 / x
        n = -n

    temp = Pow(x, n // 2)
    
    if n % 2 == 0:
        return temp * temp
    else:
        return temp * temp * x

print(Pow(2.00000, 10))   
print(Pow(2.10000, 3))    
print(Pow(2.00000, -2))   
