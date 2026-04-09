def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("=" * 35)
    print("   Welcome to the CLI Calculator!")
    print("=" * 35)

    while True:
        print("\nSelect an operation:")
        print("  1. Addition       (+)")
        print("  2. Subtraction    (-)")
        print("  3. Multiplication (*)")
        print("  4. Division       (/)")
        print("  5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("\nThank you for using the calculator. Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select a number between 1 and 5.")
            continue

        a = get_number("Enter first number:  ")
        b = get_number("Enter second number: ")

        if choice == "1":
            result = add(a, b)
            op = "+"
        elif choice == "2":
            result = subtract(a, b)
            op = "-"
        elif choice == "3":
            result = multiply(a, b)
            op = "*"
        elif choice == "4":
            result = divide(a, b)
            op = "/"

        print(f"\nResult: {a} {op} {b} = {result}")

if __name__ == "__main__":
    main()
