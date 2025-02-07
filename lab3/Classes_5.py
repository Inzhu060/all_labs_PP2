class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"New balance ({self.balance})")
        else:
            print("Amount must be positive!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal denied")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

account = Account("Arman", 150)
account.deposit(60)  
account.withdraw(45) 
account.withdraw(170)  
account.withdraw(-10)  