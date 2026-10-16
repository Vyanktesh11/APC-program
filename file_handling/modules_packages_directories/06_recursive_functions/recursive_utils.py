def factorial(n):
    if n < 0: raise ValueError("n must be non-negative")
    return 1 if n <= 1 else n * factorial(n - 1)

def fibonacci(n):
    if n <= 0: return []
    if n == 1: return [0]
    sequence = fibonacci(n - 1)
    sequence.append(sequence[-1] + (sequence[-2] if len(sequence) > 1 else 0))
    return sequence

def sum_digits(n):
    n = abs(n)
    return n if n < 10 else n % 10 + sum_digits(n // 10)

def binary(n):
    if n < 0: raise ValueError("n must be non-negative")
    return str(n) if n < 2 else binary(n // 2) + str(n % 2)
