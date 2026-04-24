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
    tokens = []
    tempNum = ""

    # 1. 토큰화 (괄호 추가)
    for char in expr:
        if char == " ": continue
        if char.isdigit() or char == ".":
            tempNum += char
        else:
            if tempNum:
                tokens.append(tempNum)
                tempNum = ""
            tokens.append(char)
    if tempNum: tokens.append(tempNum)

    # Tokenize the input expression
    for token in tokens:
        if token[0].isdigit():
            numbersToken.append(float(token))
        
        elif token == "(":  # 여는 괄호는 무조건 push
            opToken.append(token)
            
        elif token == ")":  # 닫는 괄호를 만나면
            # 여는 괄호를 만날 때까지 쌓인 연산자들을 모두 계산
            while opToken and opToken[-1] != "(":
                y = numbersToken.pop()
                x = numbersToken.pop()
                op = opToken.pop()
                numbersToken.append(operation(x, y, op))
            opToken.pop()  # 마지막에 남아있는 "("를 스택에서 제거
            
        else:  # 일반 연산자 (+, -, *, /)
            while opToken and opToken[-1] != "(" and precedence(opToken[-1]) >= precedence(token):
                y = numbersToken.pop()
                x = numbersToken.pop()
                op = opToken.pop()
                numbersToken.append(operation(x, y, op))
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

    print(f"Result: {solver(userEquation.replace(" ", ""))}")