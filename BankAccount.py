class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        """
        Initialize the bank account with an account number and an optional initial balance.
        :param account_number: str
        :param initial_balance: float
        """
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposit money into the account.
        :param amount: float
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        :param amount: float
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        """
        Check and return the current balance of the account.
        """
        print(f"Current balance: {self.balance:.2f}")
        return self.balance

# Example usage:
if __name__ == "__main__":
    # Create a new account with an initial balance of 1000
    account = BankAccount("123456789", 1000)

    while True:
        print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "4":
            print("Exiting. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")
