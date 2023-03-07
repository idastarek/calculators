def get_number():
    num1 = float(input("Give me a number: "))
    num2 = float(input("Give me another number: "))
    return num1, num2

def get_operator():
    operator = input("Give me an operator: +, -, * or / ")
    return operator


calculation = input("Do you want to do a calculation? (yes/no) ")
while calculation == "yes":

    num1, num2 = get_number()
    operator = get_operator()

    if operator == '+':
        print(float(num1) + float(num2))
    elif operator == '-':
        print(float(num1) - float(num2))
    elif operator == '*':
        print(float(num1) * float(num2))
    elif operator == '/':
        print(float(num1) / float(num2))
    elif operator != '+' or '-' or '*' or '/':
        print("Choose one of the indicated operators.")
    another_calculation = input("Do you want to do another calculation? (yes/no): ")
    if another_calculation == "no":
        print("Okay, you're done for today!")
        break

if calculation == "no":
    print("Okay, no calculating today!")
elif calculation != "yes" or calculation != "no":
    print("Invalid input!")
