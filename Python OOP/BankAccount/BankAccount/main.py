class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds..."
        self.balance -= amount
        return f"Withdrew {amount} from {self.owner_name}'s account."

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount} to {self.owner_name}'s account."

    def view_balance(self):
        return f"The account has balance: {self.balance}"

    def account_details(self):
        return f"Bank Account of {self.owner_name} has balance: {self.balance}"



owner = input("Enter owner's name: ")
balance = int(input("Enter the default balance: "))
bank_account = BankAccount(owner, balance)
print("Bank account created!")


while True:
    action = input("Withdraw/Deposit/View/Details: ").lower()

    if action == "withdraw":
        amount = int(input("Enter the withdrawal amount: "))
        print(bank_account.withdraw(amount))
    if action=="view":
        print(bank_account.view_balance())
    if action=="details":
        print(bank_account.account_details())

    elif action == "deposit":
        amount = int(input("Enter the deposit amount: "))
        print(bank_account.deposit(amount))

    else:
        print("Invalid action. Please type 'Withdraw' or 'Deposit'.")
        continue


    go_again = input("Do more? (y/n): ").lower()

    if go_again == "n":
        print("Goodbye!")
        break
    elif go_again == "y":
        continue
    else:
        print("Not a valid option. Ending session.")
        break
