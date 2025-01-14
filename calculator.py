def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Can't divide by zero")
    return x / y

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    option = input("Enter choice(1/2/3/4): ")

    if option in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if option == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif option == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif option == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif option == '4':
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(e)
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
    