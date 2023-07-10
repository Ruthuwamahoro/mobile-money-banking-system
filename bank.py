from user import User  #import User class from user module
class Bank: # Bank class to represent s banking system
    def __init__(self):
        self.users = {} #in initialise users attribute as an empty dictionary
        #and it stores a list of user account numbers
    def register_user(self, name, account_number,pin): # this function allow new user to register with bank
        if account_number not in self.users: #checking if account_number exists in a dictionary of users.
            user = User(name, account_number, pin)#if account number is unique,new User object is created with parameters
            self.users[account_number] = user #then account number is added to the users dictionary
            return user
        else:
            print("Account number already exists") #if account number already exist it prints message and returns none.
            return None
        
    def login_user(self,account_number, pin): #method that allows user to login into the account.
        if account_number in self.users: # checks if the ]account exist
            user = self.users[account_number]
            if user.pin == pin: #check if the pin matches ,return User object.
                return user
            else:
                print("Invalid PIN.")

        else:
            print("Account number does not exist")
            return None    