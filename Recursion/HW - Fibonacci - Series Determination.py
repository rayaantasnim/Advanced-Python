# Recursive function for Fibonacci
def fibonacci(n):
    if n == 0:   # base case
        return 0
    elif n == 1: # base case
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Function to generate the series up to n
def fibonacci_series(n):
    series = []
    for i in range(n):
        series.append(fibonacci(i))
    return series

# Sample usage
n = int(input("Enter the value of desired range: "))
print("Fibonacci series up to", n, "terms:")
print(fibonacci_series(n))
