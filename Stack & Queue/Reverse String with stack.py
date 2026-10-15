user_input = input("Enter a string: ")
print("Given String:", user_input)

stack = []
for char in user_input:
    stack.append(char)

reversed_text = ""
while (len(stack) > 0):
    reversed_text = reversed_text + stack.pop()

print("Reversed string:", reversed_text.title())