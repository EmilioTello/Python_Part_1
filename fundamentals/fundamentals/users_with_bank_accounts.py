class BankAccount:
    instances = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.instances.append(self)

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

    def transfer_money(self, transfer, receiver):
        self.balance -= transfer
        receiver.balance += transfer
        self.display_account_info()
        receiver.display_account_info()
        return self

    def display_account_info(self):
        return f"{self.balance}"

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self


    @classmethod
    def all_instances(cls):
        for account in cls.instances:
            account.display_account_info()
        



class User:

    bank_name = "First National Dojo"

    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.account = {
            "savings" : BankAccount(.03, 3000),
            "checking" : BankAccount(.01, 1500)
        }

    def user_deposit (self, acct, amount):
        self.account[acct].deposit(amount)

    def display_user_balance(self):
        print (f"User: {self.name}, Checking Balance: ${self.account['checking'].display_account_info()}")
        print (f"User: {self.name}, Savings Balance: ${self.account['savings'].display_account_info()}")
        return self


        

ricky = User("Ricky", "ricky@ricardo.com")
guido = User("Guido", "guido@gmail.com")

ricky.user_deposit("savings",1000)
ricky.account["savings"].deposit(1000)
ricky.account["checking"].deposit(500)
ricky.account["savings"].withdraw(200)
ricky.account["checking"].withdraw(250)
ricky.display_user_balance()


guido.account["savings"].deposit(2000)
guido.account["checking"].deposit(1000)
guido.account["savings"].withdraw(1800)
guido.account["checking"].withdraw(500)
guido.display_user_balance()


guido.account["checking"].transfer_money(150,ricky.account["checking"])
ricky.display_user_balance()
guido.display_user_balance()
