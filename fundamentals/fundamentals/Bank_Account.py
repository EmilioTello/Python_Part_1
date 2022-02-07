class BankAccount:
    # don't forget to add some default values for these parameters!
    instances = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.instances.append(self)

        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def all_instances(cls):
        for account in cls.instances:
            account.display_account_info()
        


checking = BankAccount(.01,500)
savings = BankAccount(.03,2000)

checking.deposit(1000).deposit(500).deposit(250).withdraw(750).yield_interest().display_account_info()
savings.deposit(3000).deposit(1000).withdraw(1000).withdraw(2000).withdraw(250).withdraw(500).yield_interest().display_account_info()

BankAccount.all_instances()