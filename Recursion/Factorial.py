# Factorial using Recursion
def factorial_recursive(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Factorial using Loop
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = int(input("Enter a number: "))
if(num !=0):
    print("Factorial (Recursion):", factorial_recursive(num))
    print("Factorial (Loop):", factorial_loop(num))

elif(num == 0):
    print("Factorial: 1")

else:
    print("Error Occured.")