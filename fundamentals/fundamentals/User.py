class User:

    bank_name = "First National Dojo"

    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, deposit):
        self.account_balance += deposit
    def make_withdrawal(self,withdrawal):
        self.account_balance -= withdrawal
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
    def transfer_money(self, transfer, receiver):
        self.account_balance -= transfer
        receiver.account_balance += transfer
        self.display_user_balance()
        receiver.display_user_balance()
        


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
ricky = User("Ricky Ricardo", "rickyricardo@lucy.com")


guido.make_deposit(50)
guido.make_deposit(80)
guido.make_deposit(100)
guido.make_withdrawal(20)
guido.display_user_balance()

monty.make_deposit(30)
monty.make_deposit(300)
monty.make_withdrawal(150)
monty.make_withdrawal(25)
monty.display_user_balance()

ricky.make_deposit(400)
ricky.make_withdrawal(150)
ricky.make_withdrawal(200)
ricky.make_withdrawal(25)
ricky.display_user_balance()

guido.transfer_money(75, ricky)
