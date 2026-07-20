while True:
    print("\n====Calculator====")
    print("1. Addition (+) ")
    print("2. Subtraction (-) ")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("Type 'exit' to quit")

    choice = input("Enter choice: ")

    if choice.lower() == "exit":
        print("Goddbye")
        break

    if choice not in ["1","2","3","4"]:
        print("Invalid choice!")
        continue

    try:
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))

        if choice == "1":
            print(f"Result: {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1 * num2}")
        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                print(f"Result: {num1/num2}")

    except ValueError:
        print("Please enter valid numbers!")
