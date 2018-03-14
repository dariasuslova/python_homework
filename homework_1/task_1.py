def fibonacci(n):
    if n.__class__ is not int:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    x, y = 0, 1
    for i in range (n):
        x, y = y, x+y
    return x

print(fibonacci(6))
