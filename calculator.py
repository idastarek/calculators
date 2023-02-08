calculation = input("Wanna do a calculation? (yes/no) ")
while calculation == "yes":

    number1 = float(input("Give me a number: "))
    operator = input("Give me an operator: +, -, * or / ")
    number2 = float(input("Give me another number: "))
    print(number1, operator, number2)

    if operator == '+':
        print(float(number1) + float(number2))
    elif operator == '-':
        print(float(number1) - float(number2))
    elif operator == '*':
        print(float(number1) * float(number2))
    elif operator == '/':
        print(float(number1) / float(number2))
    elif operator != '+' or '-' or '*' or '/':
        print("Choose one of the indicated operators.")
    another_calculation = input("Wanna do another calculation? (yes/no): ")
    if another_calculation == "no":
        print("Okay, you're done for today!")
        break


if calculation == "no":
    print("Okay, no calculating today!")
elif calculation != "yes" or "no":
    print("Invalid input!")





