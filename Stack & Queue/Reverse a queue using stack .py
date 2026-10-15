queue = [10, 20, 30, 40, 50]
stack = []

while (queue):
    stack.append(queue.pop(0))

while (stack):
    queue.append(stack.pop())

print(queue)
