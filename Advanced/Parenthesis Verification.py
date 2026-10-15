bracket_map = {
    "(": ")",
    "{": "}",
    "[": "]"
}

stack = []
st = input("Enter the parenthesis: ")

balanced = True
for ch in st:
    if ch in "({[":
        stack.append(ch)

    elif ch in ")}]":
        if len(stack) == 0:
            balanced = False
            break 

        top = stack.pop()

        if bracket_map[top] != ch:
            balanced = False
            break

if len(stack) != 0:
    balanced = False

if balanced and len(stack) == 0:
    print("The parentheses are balanced.")
else:
    print("The parentheses are NOT balanced.")
