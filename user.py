class User: #creating user class representing use in the banking system
    def __init__(self, name,account_number, pin): #initializing attributes
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = 0.0
        self.transaction_history = []

    def deposit (self,amount):#defining function that allow user to deposit amount
        self.balance += amount
        self.transaction_history.append(f"Deposit: +{amount}")
    def withdraw(self, amount): # withdraw specific amount from account
        if amount <= self.balance:
            self.balance -=amount
            self.transaction_history.append(f"withdraw: -{amount}")
        else:
            print("Insufficient funds.")
    def get_balance(self): #return current balance of the user
        return self.balance
    def get_transaction_history(self): #return transaction history
        return self.transaction_history    