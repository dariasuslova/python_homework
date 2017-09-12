def fibonacci(n):
    if n.__class__ is not int:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
