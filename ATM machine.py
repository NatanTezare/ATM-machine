import hashlib
from datetime import datetime

# Function to hash the PIN
def hash_pin(pin):
    return hashlib.sha256(str(pin).encode()).hexdigest()

# Function to verify PIN
def verify_pin(stored_hash, pin):
    return stored_hash == hash_pin(pin)

# Account data structure
accounts = {
    "123456789": {
        "balance": 100000,
        "pin_hash": hash_pin(543210),
        "transactions": [],
        "time":[]
    },
    "987654321": {
        "balance": 50000,
        "pin_hash": hash_pin(123456),
        "transactions": [], 
        "time":[]
    }
}

incorrect_attempts = 0

def check_balance(account):
    print(f"Your balance is {accounts[account]['balance']} ksh only.")

def deposit(account):
    deposit_amount = float(input("Enter the amount you want to deposit here: "))
    accounts[account]['balance'] += deposit_amount
    accounts[account]['transactions'].append(f"Deposited {deposit_amount} ksh")
    accounts[account]['time'].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(f"Transaction Successful, you have successfully deposited {deposit_amount}. Your new balance is {accounts[account]['balance']} ksh.")

def withdraw(account):
    withdraw_amount = float(input("Enter the amount you want to withdraw here: "))
    if withdraw_amount > 50000:
        print("You have exceeded the maximum amount to withdraw, which is 50000 ksh.")
    elif withdraw_amount <= accounts[account]['balance']:
        accounts[account]['balance'] -= withdraw_amount
        accounts[account]['transactions'].append(f"Withdrew {withdraw_amount} ksh")
        accounts[account]['time'].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(f"Transaction Successful, you have successfully withdrawn {withdraw_amount}. Your new balance is {accounts[account]['balance']} ksh.")
    else:
        print("Insufficient balance for this withdrawal.")

def view_transactions(account):
    print("\nTransaction History:")
    if accounts[account]['transactions'] and accounts[account]['time']:
        for transaction, dateTime in zip(accounts[account]['transactions'], accounts[account]['time']):
            print(f"{dateTime} - {transaction}")
    else:
        print("No transactions available.")

def authentication(account):
    global incorrect_attempts
    pin = int(input("Enter your PIN here: "))
    if verify_pin(accounts[account]['pin_hash'], pin):
        print("Login successful")
        return True
    else:
        incorrect_attempts += 1
        print(f"Incorrect PIN. You have {3 - incorrect_attempts} attempts left.")
        return False
    
def change_pin(account):
    pin = int(input("Enter your current PIN here: "))
    if verify_pin(accounts[account]['pin_hash'], pin):
        new_pin = int(input("Enter your new PIN here: "))
        confirm_pin = int(input("Confirm your new PIN: "))
        
        if new_pin == confirm_pin:
            if hash_pin(new_pin) == accounts[account]['pin_hash']:
                print("The new PIN cannot be the same as the current PIN.")
            else:
                accounts[account]['pin_hash'] = hash_pin(new_pin)
                print("Your PIN has been successfully changed.")
        else:
            print("Confirmation PIN does not match the new PIN.")
    else:
        print("Invalid PIN. Please try again.")


def atm_machine():
    global incorrect_attempts
    print("Insert your card (Enter your account number)")
    account = input("Enter your account number: ")

    if account in accounts:
        while incorrect_attempts < 3:
            if authentication(account):
                while True:
                    print("\nEnter 1 for Balance Inquiry")
                    print("Enter 2 for Money Deposit")
                    print("Enter 3 for Money Withdrawal")
                    print("Enter 4 for Transaction History")
                    print("Enter 5 for Changing Pin")
                    print("Enter 6 to Quit")

                    option = int(input("Select your option (1/2/3/4/5) here: "))

                    if option == 1:
                        check_balance(account)
                    elif option == 2:
                        deposit(account)
                    elif option == 3:
                        withdraw(account)
                    elif option == 4:
                        view_transactions(account)
                    elif option == 5:
                        change_pin(account)
                    elif option == 6:
                        print("Exiting the ATM machine. Goodbye!")
                        return
                    else:
                        print("Invalid option. Please try again.")
            else:
                if incorrect_attempts >= 3:
                    print("Maximum incorrect PIN attempts reached. Account locked.")
                    return
    else:
        print("Account not found.")


atm_machine()
