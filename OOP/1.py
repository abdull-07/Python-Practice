# Create a BankAccount class (deposit, withdraw, show balance)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}, New balance is {self.balance}")
        else:
            print("Deposit amount must be positive.")
            
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufizent Balance:")
        else:
            if amount > 0:
                self.balance -= amount
                print(f"withdraw amount {amount}, New balance is {self.balance}")
            else:
                print("Withdraw amount must be positive")
                
    def show_balance(self):
        print(f"Current Balance is {self.balance}")
        
    def get_owner(self):
        return self.owner

acc1= BankAccount("Muhammad Abdullah", 10000)
print(acc1.deposit(5000))