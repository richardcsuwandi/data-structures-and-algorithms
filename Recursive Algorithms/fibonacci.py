# Create an empty dict to store cached values
fibonacci_cache = {}

def fibonacci(n):
    # If the value is cached, return the value
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # Compute the nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
    # Cache the value and return
    fibonacci_cache[n] = value
    return value

def main():
    for n in range(1, 101):
        print(f'{n}: {fibonacci(n)}')

if __name__ == "__main__":
    main()