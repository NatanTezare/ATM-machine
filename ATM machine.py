def check_balance():
    global balance
    print("Your balance is ",balance," ksh only.")

def deposit():
    global balance
    deposit_amount=float(input("Enter the amount you want to deposit here:"))
    balance += deposit_amount
    print("Transaction Successful, you have successfully deposited",deposit_amount,". And now your balance is",balance)

def withdraw():
    global balance
    withdraw_amount=float(input("Enter the amount you want to withraw here:"))
    if withdraw_amount > 50000:
        print("You have exceeded the maximum amount to withdraw which is 50000")
    elif withdraw_amount <= balance:
        balance-=withdraw_amount
        print("Transaction Successful, you have successfully withdrawed ",withdraw_amount,". And now your balance is",balance)
    else:
        print("You have Insufficient balance for this withrawal")
    

def authentication():
    global incorrect_attempts
    pin = int(input("Enter your PIN here: "))
    if pin == stored_pin:
        print("Login successful")
        return True
    else:
        incorrect_attempts += 1
        print(f"Incorrect PIN. You have {3 - incorrect_attempts} attempts left.")
        return False

stored_pin = 543210
balance = 100000
incorrect_attempts = 0

print("Insert your card")

while incorrect_attempts < 3:
    if authentication():
        while True:
            print("\nEnter 1 for Balance Inquiry")
            print("Enter 2 for Money Deposit")
            print("Enter 3 for Money Withdrawal")
            print("Enter 4 to Quit")

            option = int(input("Select your option (1/2/3/4) here: "))

            if option == 1:
                check_balance()
            elif option == 2:
                deposit()
            elif option == 3:
                withdraw()
            elif option == 4:
                print("Exiting the ATM machine. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        if incorrect_attempts >= 3:
            print("Maximum incorrect PIN attempts reached. Account locked.")
            break