from art import logo


def add(n1, n2):
    return n1 + n2

#TODO: Write out the other 3 functions
# - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2



#TODO: Add these 4 functions into a dictionary as the values.
# Keys = "+", "-", "*", "/"
Operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# TODO: Use the dictionary operations to perform the calculations.
#  Multiply 4 * 8 using the dictionary.
def calculator():
    print(logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in Operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What is the next number?: "))

        answer = Operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 4)
            calculator()

calculator()

