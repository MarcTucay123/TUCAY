class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient balance for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Account Balance: ${self.balance}")

# Create a BankAccount instance
account = BankAccount(account_number="12345678", owner="John Doe", balance=500)

# Let the user input how much they want to deposit or withdraw
while True:
    print("\nChoose an action:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    action = input("Enter the number of the action you want to perform: ")

    if action == "1":
        try:
            deposit_amount = float(input("Enter amount to deposit: "))
            account.deposit(deposit_amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    elif action == "2":
        try:
            withdraw_amount = float(input("Enter amount to withdraw: "))
            account.withdraw(withdraw_amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    elif action == "3":
        account.display_balance()
    
    elif action == "4":
        print("Exiting the system.")
        break

    else:
        print("Invalid action. Please choose a valid option.")
