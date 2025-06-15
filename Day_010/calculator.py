from art import logo

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

def calculator(f_number):
    for key in operations:
        print(key)
    operator = input("Pick an operation: ")
    next_number = float(input("What is the next number? "))
    result = operations[operator](f_number, next_number)
    print(f"{f_number} {operator} {next_number} = {result}")

    continue_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a "
                                 f"new calculation: ").lower()

    if continue_calculation == "y":
        f_number= result
        calculator(f_number)


print(logo)
operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
}

first_number = float(input("Please enter the first number: "))
calculator(first_number)
