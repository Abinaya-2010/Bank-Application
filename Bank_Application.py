#Base class

class Account:
    def __init__(self):
        self.cust_id = 0
        self.balance = 0.0

# SBAccount for Savings account, derived from Account

class SBAccount(Account):

    def __init__(self, cust_id, balance):  #parameterized constructer
        super().__init__()
        self.balance = balance
        self.cust_id = cust_id
        print("\n✅ New SB Account Created Successfully!")
        print("-------------------------------------------")
        print(f"🧾 Customer ID   : {cust_id}")
        print(f"💰 Balance       : {balance:.2f}")
        print("🔒 Customer ID is confidential. Keep it safe!")
        print("-------------------------------------------\n")

    def deposit(self, dep_amt):   #Deposit method to add amount to existing balance
        if dep_amt > 0:
            print(f"\nAvailable Balance : ₹{self.balance:.2f}")
            self.balance += dep_amt
            print(f"✅ Amount Deposited : ₹{dep_amt:.2f}")
            print(f"💰 New Balance      : ₹{self.balance:.2f}\n")
        else:
            print("\n❌ Invalid Amount\n")

    def withdraw(self, with_amt):   #Withdraw method to withdraw amount with minimum balance check
        if self.balance > with_amt + 1000:
            print(f"\nAvailable Balance : ₹{self.balance:.2f}")
            self.balance -= with_amt
            print(f"✅ Amount Withdrawn : ₹{with_amt:.2f}")
            print(f"💰 New Balance      : ₹{self.balance:.2f}\n")
        else:
            print("\n❌ Insufficient Balance\n")

    def calc_interest(self):   #Calculate 4% annual interest and credits it
        print(f"\nAvailable Balance : ₹{self.balance:.2f}")
        interest = 0.04 * self.balance / 12
        print(f"📈 Monthly Interest (4% p.a) : ₹{interest:.2f}")
        self.balance += interest
        print(f"💰 New Balance               : ₹{self.balance:.2f}\n")


# FDAccount for Fixed Deposit, derived from Account


class FDAccount(Account):
    def __init__(self, period, cust_id, balance):    #Parameterized constructor
        self.period = period
        super().__init__()
        self.cust_id = cust_id
        self.balance = balance
        print("\n✅ New FD Account Created Successfully!")
        print("-------------------------------------------")
        print(f"🧾 Customer ID : {cust_id}")
        print(f"💰 Balance     : {balance:.2f}")
        print(f"🕒 Period      : {period} months")
        print("🔒 Customer ID is confidential. Keep it safe!")
        print("-------------------------------------------\n")

    def calc_interest(self):     # Calculates interest at 8.25% p.a. for the given period 
        interest = 0.0825 * self.balance * self.period / 12
        print(f"\n💰 FD Balance          : ₹{self.balance:.2f}")
        print(f"📈 Interest for {self.period} months : ₹{interest:.2f}\n")
        return interest

    def close(self):     # Closes FD and credits interest to balance
        self.balance += self.calc_interest()
        print(f"✅ FD Closed. New Balance : ₹{self.balance:.2f}")

# Customer class to hold personal data and associated accounts

class Customer:
    def __init__(self, cust_id, name, address):    #Parameterized Constructor
        self.cust_id = cust_id
        self.name = name
        self.address = address
        self.balance = 0
        self.period = 0
        self.sb = None     # SBAccount object
        self.fd = None     # FDAccount object

    def createAccount(self, val):    # Create SB or FD account based on user choice
        if val == 1:
            self.balance = float(input("Enter Initial Balance : ₹"))
            self.sb = SBAccount(self.cust_id, self.balance)
        elif val == 2:
            self.balance = float(input("Enter Initial Balance : ₹"))
            self.period = int(input("Enter Period (in months) : "))
            self.fd = FDAccount(self.period, self.cust_id, self.balance)
        else:
            print("\n❌ Invalid Choice\n")

    def transaction(self, val):     # Perform a transaction: deposit, withdraw, interest, or close FD
        if val == 1:
            amt = float(input("Enter Amount to be Deposited : ₹"))
            self.sb.deposit(amt)
        elif val == 2:
            amt = float(input("Enter Amount to Withdraw : ₹"))
            self.sb.withdraw(amt)
        elif val == 3:
            self.sb.calc_interest()
        elif val == 4:
            print("FD Account closed successfully.")
            self.fd.close()
        else:
            print("\n❌ Invalid Choice\n")


#Main Program starts here

c = []     #List to store customer objects
i = 0
cust_id = 7580467   #Starting customer ID

print("****************************************************************")
print("                  🌟 Welcome to AVB Bank 🌟                     ")
print("****************************************************************")

while True:
    #Main Menu
    print("\n🏦 Main Menu")
    print("1. SB Account")
    print("2. FD Account")
    print("3. Exit")
    ch1 = int(input("Enter your choice: "))

    if ch1 == 1:
        ch2 = 0
        while ch2 != 5:
            # SB Account menu
            print("\n📘 SB Account Menu")
            print("1. Open New SB Account")
            print("2. Deposit to SB Account")
            print("3. Withdraw from SB Account")
            print("4. Calculate SB Interest")
            print("5. Exit to Main Menu")
            ch2 = int(input("Enter your choice: "))

            if ch2 == 1:
                name = input("Enter your Name     : ")
                address = input("Enter your Address  : ")
                c.append(Customer(cust_id + i, name, address))
                c[i].createAccount(1)
                i += 1
            elif ch2 == 2:
                cid = int(input("Enter Customer ID   : "))
                c[cid - cust_id].transaction(1)
            elif ch2 == 3:
                cid = int(input("Enter Customer ID   : "))
                c[cid - cust_id].transaction(2)
            elif ch2 == 4:
                cid = int(input("Enter Customer ID   : "))
                c[cid - cust_id].transaction(3)
            elif ch2 == 5:
                print("\n👋 Thanks for using SB Account Services.\n")
            else:
                print("\n❌ Invalid Choice\n")

    elif ch1 == 2:
        ch3 = 0
        while ch3 != 3:
            # FD Account menu
            print("\n📙 FD Account Menu")
            print("1. Open New FD Account")
            print("2. Close FD Account")
            print("3. Exit to Main Menu")
            ch3 = int(input("Enter your choice: "))

            if ch3 == 1:
                name = input("Enter your Name     : ")
                address = input("Enter your Address  : ")
                c.append(Customer(cust_id + i, name, address))
                c[i].createAccount(2)
                i += 1
            elif ch3 == 2:
                cid = int(input("Enter Customer ID   : "))
                c[cid - cust_id].transaction(4)
            elif ch3 == 3:
                print("\n👋 Thanks for using FD Account Services.\n")
            else:
                print("\n❌ Invalid Choice\n")

    elif ch1 == 3:
        print("\n🙏 Thank you for banking with AVB Bank. Have a great day! 😊")
        break
    else:
        print("\n❌ Invalid Choice\n")
