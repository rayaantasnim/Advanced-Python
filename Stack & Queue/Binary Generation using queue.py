def generate_bin(n):
    q = ["1"]

    for i in range(n):
        current = q.pop(0)
        print(current)
        q.append(current + "0")
        q.append(current + "1")

a = int(input("How many numbers you want: "))
generate_bin(a)