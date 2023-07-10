from bank import  Bank # import Bank class from bank module
bank = Bank() #  creating  instances of Bank class

def register_user():
    name = input("Enter your name: ")
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")
    user = bank.register_user(name, account_number, pin)
    if user:
        print(f"User {user.name} registered successful.")
def login_user():
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN :")
    user = bank.login_user(account_number, pin)
    if user:
        show_menu(user)

def show_menu(user):
    if user:
        print("\n[1] Deposit")
        print("[2] Withdraw")
        print("[3] Check Balence")
        print("[4] Transaction History")
        print("[5] Logout")

    choice = input("Enter your choice: ")
    if choice == "1":
        amount = float(input("Enter the amount to deposit: "))
        user.deposit(amount)
        print("Deposit successful.")
    elif choice =="2":
        amount = float(input("Enter the amount to withdraw: "))
        user.withdraw(amount)
        print("Withdrawl successful.")
    elif choice == "3":
        balance=user.get_balance()
        print(f"Current balance: {balance}")
    elif choice == "4":
        history = user.get_transaction_history()
        print("Transaction history: ")
        for transaction in history:
            print(transaction)

    elif choice == "5":
        print("Input Error.")
def main():
    while True:
        print("\n[1] Register")
        print("[2] Login")
        print("[3] Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            break

if __name__ == "__main__":
    main()