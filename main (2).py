#python program to create   Bankaccount class
#with both a deposit() and   withdraw() function
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to  the Deposit & Withdrawal Machine")

    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print(" \n AmountDeposited:",amount)

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:",amount)
        else:
          print("\n Insufficient balance  ")

    def display(self):
          print("\n Net AvailableBalance=",self.balance)

#Driver code

#creating an object of class
s = Bank_Account()

#calling functions with that class object
s.deposit()
s.withdraw()
s.display()