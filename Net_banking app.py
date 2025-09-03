import datetime as dt
import os
file="Bank_Records"

class bank:
    def __init__(self,intial_balance=1000.00):
        self.balance=intial_balance

        if os.path.exists(file):
            with open(file,"r") as f:
                lines=f.readlines()
                if lines:
                    last_line=lines[-1].strip().split("|")
                    self.balance=float(last_line[-1].split("Rs.")[1])
        

    def record_transactions(self,transaction):
        date=dt.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        data=open(file,"a")
        data.write(f"{date}-{transaction}\n")
     

    def deposit(self,amount):
        self.balance+=amount
        print(f"Amount Deposited Successfully-Rs.{amount}")
        self.record_transactions(f"Amount Deposited Rs.{amount} | Current balance Rs.{self.balance}")

        check=input("Do you want see your balance(Yes or No):")
        if check=="yes" or check=="Yes" or check=="YES":
            print(f"Current balance:Rs.{self.balance}\n")
        elif check=="no" or check=="No" or check=="NO":
            print(f"Thank You!\n")
        else:
            print("Invalid\n")


    def withdraw(self,amount):
        if self.balance<=0:
            print("Insifficent balance....\n")
        else:
            self.balance-=amount
            print(f"Rs.{amount} withdraw")
            self.record_transactions(f"Amount Withdrawl Rs.{amount} | Current balance Rs.{self.balance}")

            check=input("Do you want see your balance(Yes or No):")
            if check=="yes" or check=="Yes" or check=="YES":
                print(f"Current balance:Rs.{self.balance}\n")
            elif check=="no" or check=="No" or check=="NO":
                print(f"Thank You!\n")
            else:
                print("Invalid\n")


net_bank=bank()
print("Welcome to net banking app!\n\t----Menu----")
print("1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit")

while True:
    try:
        user=int(input("Enter your choice(1-4):"))

        if user==1:
            amount=float(input("Enter the amount:"))
            net_bank.deposit(amount)
        elif user==2:
            amount=float(input("Enter the amount:"))
            net_bank.withdraw(amount)
        elif user==3:
            print(f"Your current balance Rs.{net_bank.balance}\n")
        elif user==4:
            print("Thank you for using net banking")
            break
        else:
            print("Invalid input.Try again!\n")
    except:
        print("Invaild Input.Try Again!\n")

