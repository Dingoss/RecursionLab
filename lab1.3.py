def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n1 = 2
n2 = 3
n3 = 4

print("F(", n1, ") =", fibonacci(n1))
print("F(", n2, ") =", fibonacci(n2))
print("F(", n3, ") =", fibonacci(n3))
