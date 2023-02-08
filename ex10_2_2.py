import getpass

supplied_pin = getpass.getpass(prompt="Enter your PIN: ")

answer = "1234"


if supplied_pin == answer:
    print("PIN accepted!")

else:
    attempt = 1
    supplied_pin = getpass.getpass(prompt="PIN code incorrect. You have 2 more attempts.")
    if supplied_pin == answer:
            print("PIN accepted!")
    else:
        attempt = 2
        supplied_pin = getpass.getpass(prompt="PIN code incorrect. You have 1 more attempt.")
        if supplied_pin == answer:
            print("PIN accepted")
        else:
            attempt = 3
            print("PIN is incorrect. You've exceeded your number of attempts.")




