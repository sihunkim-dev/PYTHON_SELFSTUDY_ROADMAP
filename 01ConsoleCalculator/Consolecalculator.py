print("Hello, welcome to the console calculator!")

equationSolver = []

def operation(x, y, operator):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        if y != 0:
            return x / y
        else:
            print("Error: Division by zero is not allowed.")
            return None
    else:
        print("Invalid operator.")
        return None

def precedence(operator):
    if operator in ("+", "-"):
        return 1
    elif operator in ("*", "/"):
        return 2
    else:
        return 0

def solver(expr):
    numbersToken = []
    opToken = []

    tokens = expr.split()

    # Tokenize the input expression
    for token in tokens:
        if token.isdigit():
            numbersToken.append(float(token))
        else:
            while opToken and precedence(opToken[-1]) >= precedence(token):
                x = numbersToken.pop()
                y = numbersToken.pop()
                operator = opToken.pop()
                numbersToken.append(operation(y, x, operator))
            opToken.append(token)

    while opToken:
        x = numbersToken.pop()
        y = numbersToken.pop()
        operator = opToken.pop()
        numbersToken.append(operation(y, x, operator))

    return numbersToken[0]
    


# Simple console Calculator while True:
while True:    
    quit = input("Enter q for quit: ")
    print(quit)
    if quit == "q":
        print("Goodbye!")
        break

    userEquation = input("Enter your equation: ")
    result = print(userEquation)

    print(f"Result: {solver(userEquation)}")