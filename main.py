def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        return None
    return a / b


if __name__ == "__main__":
    print("Simple Calculator")

    a = float(input("First number: "))
    b = float(input("Second number: "))

    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Division:", divide(a, b))
