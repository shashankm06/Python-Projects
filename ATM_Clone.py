balance = 5000
pin = 3225
attempts = 0

while attempts < 3:
    try:
        enter_pin = int(input("Enter PIN: "))
    except ValueError:
        print("PIN must be numbers only!")
        attempts += 1
        continue

    if enter_pin == pin:
        print("1. Check Balance")
        print("2. Cash Withdrawal")

        try:
            query = int(input("Choose your action (1/2): "))
        except ValueError:
            print("Invalid input, numbers only!")
            continue

        if query == 1:
            print("Your balance is:", balance)

        elif query == 2:
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Amount must be a number!")
                continue

            if amount <= balance:
                balance -= amount
                print("Amount successfully withdrawn!")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient balance!")

        else:
            print("Invalid menu option")

        break  

    else:
        attempts += 1
        print("Incorrect PIN")

        if attempts == 3:
            print("Your card is blocked!")
