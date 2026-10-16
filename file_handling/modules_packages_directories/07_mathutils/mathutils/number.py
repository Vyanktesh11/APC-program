def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))
def is_palindrome(n): return str(n) == str(n)[::-1]
def is_armstrong(n):
    s = str(n)
    return n == sum(int(d) ** len(s) for d in s)
