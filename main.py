def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the division of two numbers."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def get_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


def get_operation():
    """Get a valid mathematical operation from the user."""
    valid_operations = ["+", "-", "*", "/"]

    while True:
        operation = input(
            "\nChoose an operation (+, -, *, /): "
        ).strip()

        if operation in valid_operations:
            return operation

        print("❌ Invalid operation. Please choose +, -, * or /.")


def calculate(a, b, operation):
    """Perform the selected mathematical operation."""
    if operation == "+":
        return add(a, b)

    elif operation == "-":
        return subtract(a, b)

    elif operation == "*":
        return multiply(a, b)

    elif operation == "/":
        return divide(a, b)


def main():
    """Run the calculator application."""

    print("=" * 40)
    print("       SIMPLE CALCULATOR")
    print("=" * 40)

    while True:
        print("\nAvailable operations:")
        print("  +  Addition")
        print("  -  Subtraction")
        print("  *  Multiplication")
        print("  /  Division")

        print()

        a = get_number("Enter the first number: ")
        operation = get_operation()
        b = get_number("Enter the second number: ")

        try:
            result = calculate(a, b, operation)

            print("\n" + "-" * 40)
            print(f"Result: {a} {operation} {b} = {result}")
            print("-" * 40)

        except ZeroDivisionError:
            print("\n❌ Error: You cannot divide by zero.")

        while True:
            again = input(
                "\nWould you like to perform another calculation? (yes/no): "
            ).strip().lower()

            if again in ["yes", "y"]:
                break

            elif again in ["no", "n"]:
                print("\nThank you for using Simple Calculator! 👋")
                return

            else:
                print("❌ Please enter yes or no.")


if __name__ == "__main__":
    main()
