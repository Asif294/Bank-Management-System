import random
class Bank:
    def __init__(self):
        self.users = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_enabled = True

    def create_account(self, name, email, address, account_type):
        account_number = random.randint(100000, 999999)
        account = Account(account_number, name, email, address, account_type)
        self.users.append(account)
        return account_number

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                return True
        return False
    def user_account_number(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                return user
        return None
    def all_accounts(self):
        return self.users
    def total_balance(self):
        return self.total_balance
    def total_loan(self):
        return self.total_loan_amount
    def loan_system(self):
        self.loan_enabled = not self.loan_enabled

class Account:
    def __init__(self, account_number, name, email, address, account_type):
        self.account_number = account_number
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transaction_history = []
        self.loan_taken = 0
        self.loan_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Successfully deposited {amount} TK")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Successfully withdrew {amount} TK")
        else:
            print("Withdrawal amount exceeded")
    def check_balance(self):
        return self.balance
    def Trans_history(self):
        return self.transaction_history
    def take_loan(self, amount):
        if self.loan_count < 2 and self.balance >= amount and bank.loan_enabled:
            self.loan_taken += amount
            self.balance += amount
            self.loan_count += 1
            bank.total_loan_amount += amount
            self.transaction_history.append(f"loan {amount} Tk")
            print("Loan successfully taken!")
        elif not bank.loan_enabled:
            print("Bank loan system is  disabled")
        elif self.loan_count >= 2:
            print("You have already taken the maximum number of loans")
        elif self.balance < amount:
            print("dont have sufficient balance to take this loan")

    def transfer(self, recived_account, amount):
        recipient = bank.user_account_number(recived_account)
        if recipient:
            if self.balance >= amount:
                self.balance -= amount
                recipient.balance += amount
                self.transaction_history.append(f"Transferred {amount} TK to account {recived_account}")
                recipient.transaction_history.append(f"Received {amount} TK from account {self.account_number}")
                print("Transfer successful!")
            else:
                print("Insufficient balance ")
        else:
            print("Recipient account does not exist.")

bank = Bank()
#admin interface
def admin_operations():
    while True:
        print("\nAdmin Menu:")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View All Accounts")
        print("4. Check Total Bank Balance")
        print("5. Check Total Loan Amount")
        print("6. Loan System")
        print("7. Exit")
        admin_choice = input("Enter your choice: ")
        if admin_choice == '1':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            address = input("Enter customer address: ")
            account_type = input("Enter account type (Savings/Current): ")
            an = bank.create_account(name, email, address, account_type)
            print(f"Account create successfully. account number : {an}")

        elif admin_choice == '2':
            account_number = int(input("Enter account number to delete: "))
            if bank.delete_account(account_number):
                print("Account delete successfully.")
            else:
                print("Account not found.")
        elif admin_choice == '3':
            print("\nAll User Accounts:")
            for user in bank.all_accounts():
                print(f"Account Number: {user.account_number}, Name: {user.name}, Balance: {user.balance}, Account Type: {user.account_type}")
        elif admin_choice == '4':
            print(f"Total Bank Balance: {bank.total_balance()} TK")
        elif admin_choice == '5':
            print(f"Total Loan Amount: {bank.total_loan()} TK")
        elif admin_choice == '6':
            bank.loan_system()
            if bank.loan_enabled:
                print("Loan system enabled.")
            else:
                print("Loan system disabled.")
        elif admin_choice == '7':
            break
        else:
            print("Invalid choice")
#  User interface
def user_operations(account_number):
    user = bank.user_account_number(account_number)
    while True:
        print("\nUser Menu:")
        print("1. Deposit Amount")
        print("2. Withdraw Amount")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")
        ch = input("Enter your choice: ")
        if ch == '1':
            amount = float(input("Enter amount to deposit: "))
            user.deposit(amount)
            print("Amount deposited successfully.")
        elif ch == '2':
            amount = float(input("Enter amount to withdraw: "))
            user.withdraw(amount)
        elif ch == '3':
            print(f"Available Balance: {user.check_balance()} TK")
        elif ch == '4':
            print("Transaction History:")
            for transaction in user.Trans_history():
                print(transaction)
        elif ch == '5':
            amount = float(input("Enter amount to take as loan: "))
            user.take_loan(amount)
        elif ch == '6':
            recived_account = int(input("Enter recipient account number: "))
            amount = float(input("Enter amount to transfer: "))
            user.transfer(recived_account, amount)
        elif ch == '7':
            break
        else:
            print("Invalid choice. ")
# main menu interface
while True:
    print("\nWelcome to the Bank Management System")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    main_choice = input("Enter your choice: ")
    if main_choice == '1':
        admin_operations()
    elif main_choice == '2':
        account_number = int(input("Enter your account number: "))
        user_operations(account_number)
    elif main_choice == '3':
        break
    else:
        print("Invalid choice .")
