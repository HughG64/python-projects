# Challenge 2 — OOP:
# Build a BankAccount class that:

class BankAccount:

# Stores owner and balance (default balance = 0)
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

# Has a __str__ that prints like:
#    Fums's account — Balance: R500
    def __str__(self):
        return (f"{self.owner}'s account - Balance: R{self.balance}")

# Has a deposit(amount) method that adds to balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

# Has a withdraw(amount) method that:
    def withdraw(self, amount):
# Subtracts from balance if funds are sufficient
        if self.balance >= amount:
            self.balance = self.balance - amount
            return self.balance
# Prints "Insufficient funds" if not
        else:
            print("Insufficient funds")

# Create an account
account = BankAccount("Fums")

action = input("1 for Deposit, 2 for withdrawal: ")

if action == "1":
    account.deposit(float(input("Deposit: ")))
elif action == "2":
    account.withdraw(float(input("Withdraw: ")))
else:
    print("Wrong input")

print(account)


# account = BankAccount("Fums")

# account.deposit(500)
# print(account)

# account.deposit(200)
# print(account)

# account.withdraw(300)
# print(account)

# account.withdraw(1000)  # this one should fail
# print(account)
# Then:



# Make 2 deposits
# Attempt 2 withdrawals — one that works, one that doesn't
# Print the account after each transaction
