undo_stack = []
text = ""

while(True):
    print("Current Text: ", text)
    menu = """
        1. Add Text
        2. Undo
        3. Exit"""

    print (menu)
    choice = input("Enter your choice: ").lower()

    if (choice == "1"):
        new_text = input("\nEnter your word: ")
        undo_stack.append(text) #push
        print("Added Successfully !!! ")
        text = text + " " + new_text

    elif (choice == "2"):
        if(undo_stack):
            print(undo_stack[-1], "Undo successful, reverted to previous text.")
            text = undo_stack.pop()

        else:
            print("Nothing to undo!")
            print("Because the list is already empty!")        

    elif(choice == "3"):
        print("Exiting ... ... !!!")
        break

    else:
        print("Invalid Choice Given!")
        print("Try Again later!")