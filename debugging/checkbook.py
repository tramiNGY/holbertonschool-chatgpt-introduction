class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """Deposits a given amount into the checkbook."""
        if amount <= 0:
            print("Deposit amount must be positive!")
        else:
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Withdraws a given amount from the checkbook if sufficient funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be positive!")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Displays the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """Main function to interact with the user and perform checkbook operations."""
    cb = Checkbook()  # Create a Checkbook object
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            confirm_exit = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if confirm_exit == 'yes':
                print("Thank you for using the checkbook program. Goodbye!")
                break
            else:
                continue  # Stay in the loop if the user does not want to exit
        elif action == 'deposit':
            while True:
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    cb.deposit(amount)
                    break  # Exit the loop if deposit is successful
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
        elif action == 'withdraw':
            while True:
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    cb.withdraw(amount)
                    break  # Exit the loop if withdrawal is successful
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

