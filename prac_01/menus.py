name = input("Enter name: ")
choice = input("""(H)ello
(G)oodbye
(Q)uit
>>> """).upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid input")
    choice = input("""(H)ello
(G)oodbye
(Q)uit
>>> """).upper()
print("Finished")
