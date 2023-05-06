
def fibonacci(n: int) -> int:
    """
    Computes and returns the nth Fibonacci number.
    """
    ### Region: fibonacci.call
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    ### EndRegion