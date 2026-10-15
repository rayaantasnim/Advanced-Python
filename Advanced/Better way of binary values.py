def binary_covert(number):
    # 2. Convert it to binary (this creates the string "0b11001")
    binary_with_prefix = bin(number)

    # 3. Replace the confusing "0b" text with nothing to clean it up
    clean_binary = binary_with_prefix.replace("0b", "")

    # 4. Show the final result
    print(clean_binary)

n = int(input("How many numbers you need: "))
i = 0
for a in range(n):
    binary_covert(i)
    i +=1