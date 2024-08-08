def calculate():
    num2 = stack.pop()
    num1 = stack.pop()

    return num1, num2

postfix = ['6', '5', '2', '8', '-', '*', '2', '/', '+']
stack = []

for token in postfix:
    if token.isdecimal():
        stack.append(int(token))
    else:
        if token == '-':
            num1, num2 = calculate()
            temp = num1 - num2
            stack.append(temp)
        elif token == '+':
            num1, num2 = calculate()
            temp = num1 + num2
            stack.append(temp)
        elif token == '*':
            num1, num2 = calculate()
            temp = num1 * num2
            stack.append(temp)
        else:
            num1, num2 = calculate()
            temp = num1 / num2
            stack.append(temp)

result = stack.pop()
print(result)