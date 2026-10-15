# Fibonacci using Recursion
def fibonacci_recursive(n):
    if n == 0:   # base case
        return 0
    
    elif n == 1: # base case
        return 1

    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage
num = int(input("Enter a number: "))
print("Fibonacci number at position", num, " is:", fibonacci_recursive(num))