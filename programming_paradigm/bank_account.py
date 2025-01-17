class BankAccount:
    
    def __init__(self, account_balance = 0.0):
        self.account_balance = account_balance
        
    
    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
             
    
    def withdraw(self, amount):
        self.account_balance = self.account_balance
        if amount > self.account_balance:
            self.account_balance = self.account_balance
            return False
        else:
            self.account_balance -= amount
            return True
        

    def display_balance(self):
        print(f"Current Balance: ${float(self.account_balance)}")