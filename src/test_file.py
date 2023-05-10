def fibonacci(n: int) -> int:
    """
    Computes and returns the nth Fibonacci number.
    """
    if n == 0:
        return 1
    if n == 1:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)


def factorial(n: int) -> int:
    """
    Computes and returns the factorial of n.
    """
    ### Region: factorial.call
    if n == 0:
        return 1
    return n * factorial(n - 1)
    ### EndRegion
