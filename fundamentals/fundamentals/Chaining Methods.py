class User:

    bank_name = "First National Dojo"

    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, deposit):
        self.account_balance += deposit
        return self
    def make_withdrawal(self,withdrawal):
        self.account_balance -= withdrawal
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    def transfer_money(self, transfer, user):
        self.account_balance -= transfer
        user.account_balance += transfer
        self.display_user_balance()
        user.display_user_balance()
        


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
ricky = User("Ricky Ricardo", "rickyricardo@lucy.com")


guido.make_deposit(50).make_deposit(80).make_deposit(100).make_withdrawal(20).display_user_balance()
monty.make_deposit(30).make_deposit(300).make_withdrawal(150).make_withdrawal(25).display_user_balance()
ricky.make_deposit(400).make_withdrawal(150).make_withdrawal(200).make_withdrawal(25).display_user_balance()

guido.transfer_money(75, ricky)
