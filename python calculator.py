print("Welcome to Rain's Python Calculator!")

# Ask the user for two numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Show the choices
print("\nChoose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Ask the user to choose
choice = input("Enter 1, 2, 3, or 4: ")

# Check the user's choice
if choice == "1":
    answer = first_number + second_number
    print("Answer:", answer)

elif choice == "2":
    answer = first_number - second_number
    print("Answer:", answer)

elif choice == "3":
    answer = first_number * second_number
    print("Answer:", answer)

elif choice == "4":
    if second_number == 0:
        print("Sorry, you cannot divide by zero.")
    else:
        answer = first_number / second_number
        print("Answer:", answer)

else:
    print("Sorry, that is not a valid choice.")

print("\nThank you for using the calculator!")