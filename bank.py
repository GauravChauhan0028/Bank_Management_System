#bank management system(basic) by Gaurav Chauhan

import random

# Function to create a new account
def create_account():
    account = {}
    account["acc_no"] = random.randint(100000, 999999)  # 6-digit random account number
    account["name"] = input("Enter account holder name: ")
    account["email"] = input("Enter email: ")
    account["phone"] = input("Enter phone number: ")
    account["branch"] = input("Enter branch: ")
    account["date"] = input("Enter date (e.g., 19th Sept): ")
    account["balance"] = 0
    account["incoming"] = 0
    account["outgoing"] = 0
    
    print(f"\n Account created successfully!")
    print(f"Your Account Number: {account['acc_no']}\n")
    return account

# Deposit function
def deposit(account):
    amount = int(input("Enter amount to deposit: "))
    if amount >= 2000:
        account["balance"] += amount
        account["incoming"] += amount
        print(f" Deposit Successful: ₹{amount}")
        print(f"New Balance: ₹{account['balance']}")
    else:
        print(" Deposit failed: Minimum deposit is ₹2000")

# Withdraw function
def withdraw(account):
    amount = int(input("Enter amount to withdraw: "))
    if amount <= account["balance"]:
        account["balance"] -= amount
        account["outgoing"] += amount
        print(f" Withdrawal Successful: ₹{amount}")
        print(f"New Balance: ₹{account['balance']}")
    else:
        print(" Withdrawal failed: Insufficient balance")

# Summary
def summary(account):
    print("\n Branch Manager Summary")
    print(f"Account No: {account['acc_no']}")
    print(f"Name: {account['name']}")
    print(f"Incoming (Deposits): ₹{account['incoming']}")
    print(f"Outgoing (Withdrawals): ₹{account['outgoing']}")
    print(f"Net Balance: ₹{account['balance']}")


# --- Main Program ---
account = create_account()

while True:
    print("\n===== Banking System =====")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Show Summary (Manager)")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        deposit(account)
    elif choice == "2":
        withdraw(account)
    elif choice == "3":
        summary(account)
    elif choice == "4":
        print(" Thank you for using the Banking System")
        break
    else:
        print(" Invalid choice. Please try again.")
