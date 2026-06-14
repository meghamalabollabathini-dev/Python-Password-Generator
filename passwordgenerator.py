import random
import string

password_history = []

while True:
    print("\n========== PASSWORD GENERATOR ==========")
    print("1. Generate Password")
    print("2. View Password History")
    print("3. Check Password Strength")
    print("4. Clear Password History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nPASSWORD OPTIONS")

        length = int(input("Enter password length: "))

        include_uppercase = input(
            "Include Uppercase Letters? (yes/no): "
        ).lower()

        include_lowercase = input(
            "Include Lowercase Letters? (yes/no): "
        ).lower()

        include_numbers = input(
            "Include Numbers? (yes/no): "
        ).lower()

        include_symbols = input(
            "Include Symbols? (yes/no): "
        ).lower()

        characters = ""

        if include_uppercase == "yes":
            characters += string.ascii_uppercase

        if include_lowercase == "yes":
            characters += string.ascii_lowercase

        if include_numbers == "yes":
            characters += string.digits

        if include_symbols == "yes":
            characters += string.punctuation

        if characters == "":
            print("Please select at least one character type.")
            continue

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:")
        print(password)

        password_history.append(password)

    elif choice == "2":

        if len(password_history) == 0:
            print("No passwords generated yet.")

        else:
            print("\nPASSWORD HISTORY")

            for i in range(len(password_history)):
                print(f"{i + 1}. {password_history[i]}")

    elif choice == "3":

        password = input(
            "Enter password to check strength: "
        )

        score = 0

        if len(password) >= 8:
            score += 1

        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False

        for char in password:

            if char.isupper():
                has_upper = True

            elif char.islower():
                has_lower = True

            elif char.isdigit():
                has_digit = True

            else:
                has_symbol = True

        if has_upper:
            score += 1

        if has_lower:
            score += 1

        if has_digit:
            score += 1

        if has_symbol:
            score += 1

        print("\nPASSWORD ANALYSIS")

        if score <= 2:
            print("Weak Password")

        elif score <= 4:
            print("Medium Password")

        else:
            print("Strong Password")

    elif choice == "4":

        confirm = input(
            "Clear all password history? (yes/no): "
        ).lower()

        if confirm == "yes":
            password_history.clear()
            print("Password history cleared.")

        else:
            print("Operation cancelled.")

    elif choice == "5":
        print("Thank you for using Password Generator!")
        break

    else:
        print("Invalid choice. Please try again.")