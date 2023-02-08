supplied_pin = input("Enter your PIN: ")

answer = "1234"
attempt =0

if supplied_pin == answer:
    print("PIN accepted!")

else:
    while supplied_pin != answer and attempt < 2:
        attempt = attempt + 1
        print("You have used " + str(attempt) + "attempts")
        supplied_pin = input("PIN code incorrect. Please try again.")
        if supplied_pin == answer:
            print("PIN accepted!")
        elif attempt == 3:
            print("You've acceded your number of attempts.")
