def caching_fibonacci():
    # Create an empty dictionary
    cache = {}

    # Define the inner function fibonacci
    def fibonacci(n):
        # Base cases
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # Check cache
        elif n in cache:
            return cache[n]

        # Compute Fibonacci recursively
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
