def binary_convert(number):
    print(bin(number).replace("0b", ""))

n = int(input("How many numbers you need: "))
for i in range(n):
    binary_convert(i)
