from art import logo
print(logo)

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

operation_symbol = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

end_calculation = False
first_number = int(input("What's the first number?: "))

# display all operation symbols
for operations in operation_symbol:
    print(operations)

while not end_calculation:
    operation = input("Pick an operation: ")
    next_number = int(input("What's the next number?: "))
        
    # Perform calculation
    calculation = operation_symbol[operation] # getting corresponding function
    answer = calculation(first_number, next_number)

    print(f"{first_number} {operation} {next_number} = {answer}")

    choice = input(f"Typep 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

    if choice  == 'y':
        first_number = answer #conntiniue with previous answer
    else:
        end_calculation = True
    