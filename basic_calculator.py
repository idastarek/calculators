calculation = input("Do you want to do a calculation? (yes/no) ")
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

    else:
        print("Choose one of the indicated operators.")

    another_calculation = input("Do you want to do another calculation? (yes/no): ")
    if another_calculation == "no":
        print("Okay, you're done for today!")
        break

#    calculation = input("Do you want to do a calculation? (yes/no) ")


if calculation =="no":
    print("Okay, no calculating today!")

elif calculation != "yes" and calculation != "no":
    print("Invalid input!")