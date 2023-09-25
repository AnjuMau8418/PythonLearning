# Make a Calculator
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {"+": add,
             "-": subtract,
             "*": multiply,
             "/": divide
             }


def Calculator():
    num1 = eval(input("Enter the number : "))
    for symbol in operation:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation symbol: ")
        num2 = eval(input("What is the next number? : "))
        calculation_function = operation[operation_symbol]

        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        option = input(f"Type 'y',to continue calculating with {answer},or type 'n' to start new calculation.:")
        if  option == 'y':
            num1 = answer
        elif option == 'n':
            should_continue = False
            Calculator()
        else:
            should_continue = False


Calculator()

