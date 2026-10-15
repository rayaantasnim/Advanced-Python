stack = []
d = int(input("Enter the number here: "))

while (d>0):
    r = d%2
    stack.append(r)
    d = d//2

b = ""

while(stack):
    b += str(stack.pop())

print(b)