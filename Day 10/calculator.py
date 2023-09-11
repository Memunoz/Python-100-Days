import os


def clear():
    os.system('clear')


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("Insert first number: "))
    should_continue = True

    while should_continue:
        operation = input("Select operator: ")
        num2 = float(input("Insert next number: "))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()
