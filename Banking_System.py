class Account:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self):
        Acc_No = input("Re_Enter your account No:")
        self.dep=float(input("Enter the depositing Amount:"))
        with open(f"{Acc_No}", "r+") as f:
            Balance = f.read().split()
            self.balance = float(Balance[-1])
            self.balance+=self.dep
            from datetime import datetime
            dnt = datetime.now()
            dnt = (f"{dnt.day}-{dnt.month}-{dnt.year}        {dnt.hour}:{dnt.minute}:{dnt.second}          ")
            trans_list = [dnt, self.balance]
            for i in trans_list:
                if i == trans_list[-1]:
                    f.write(str(i) + "\n")
                else:
                    f.write(f"{i}")
        print(self.balance)
    def withdraw(self):
        Acc_No = input("Re-Enter your account No: ")
        self.withdrawl=float(input("Enter the withdrawl Amount: "))
        with open(f"{Acc_No}", "r+") as f:
            Balance = f.read().split()
            self.balance = float(Balance[-1])
            if self.balance < self.withdrawl :
                print("You have insufficient balance to complete this transaction")
            else:
                self.balance -= self.withdrawl
                from datetime import datetime
                dnt = datetime.now()
                dnt = (f"{dnt.day}-{dnt.month}-{dnt.year}        {dnt.hour}:{dnt.minute}:{dnt.second}          ")
                trans_list = [dnt, self.balance]
                for i in trans_list:
                    if i == trans_list[-1]:
                        f.write(str(i) + "\n")
                    else:
                        f.write(f"{i}")
                print(self.balance)
    def balanceEnquiery(self):
        Acc_No=input("Enter your account No:")
        with open(f"{Acc_No}","r") as A:
            Balance=A.read().split()
            self.balance=float(Balance[-1])
            print("Your current balance is:",self.balance)

    def transaction(self):
        print("Press 'D' or 'd' for Deposit")
        print("Press 'W' or 'w' for Withdraw")
        choice = input("Do you want to deposit or withdraw:")
        if choice == "d" or choice == "D":
            self.deposit()
        elif choice == "w" or choice == "W":
            self.withdraw()
        else:
            pass
    def show_Account_details(self):
        Acc_No=input("Enter your CNIC No:")
        f=open(f"{Acc_No}","r")
        print(f.read())
    def show_Transaction_details(self):
        Acc_No = input("Enter account No:")
        with open(f"{Acc_No}", "r") as f:
            f=f.read()
            print(f)
class Customer:
    def __init__(self):
        self.comp=Account()
    def account_type(self):
        print("Press 1 for Checking_Account \nPress 2 for Saving_Account \nPress 3 for Loan_Account")
        self.acc_type = int(input("Enter the account type: "))
        if self.acc_type == 1:
            obj = Checking_Account()
            Customer.set_acc_details(self)
        elif self.acc_type == 2:
            obs = Saving_Account()
            Customer.set_acc_details(self)
        elif self.acc_type == 3:
            obl = Loan_Account()
            if Customer.set_acc_details(self) == True:
                obl.set_monthly_debit()
    def set_acc_details(self):
        #for userinput
        self.username = input("Enter a suitable username:")
        self.password = input("Enter a strong password:")
        self.first_name = input("Enter Your First Name:")
        self.last_name = input("Enter Your Last Name:")
        self.address = input("Enter your complete address:")
        self.CNIC = input("Enter your CNIC NO:")
        with open(f"{self.CNIC}","a+") as infoFile:
            if self.acc_type == 1:
                infoFile.write(f"              {self.username}(Checking_Account)\n"
                               f"Username:{self.username}\n"
                               f"Password:{self.password}\n"
                               f"First Name:{self.first_name}\n"
                               f"Last Name:{self.last_name}\n"
                               f"Address:{self.address}\n"
                               f"CNIC:{self.CNIC}")
                # for administrator details
                with open("Administrator.details.txt", "a+") as admin:
                    admin.write(f"              {self.username}(Checking_Account)\n"
                               f"Username:{self.username}\n"
                               f"Password:{self.password}\n"
                               f"First Name:{self.first_name}\n"
                               f"Last Name:{self.last_name}\n"
                               f"Address:{self.address}\n"
                               f"CNIC:{self.CNIC}\n\n\n")
            elif self.acc_type == 2:
                infoFile.write(f"               {self.username}(Saving_Account)\n"
                               f"Username:{self.username}\n"
                               f"Password:{self.password}\n"
                               f"First Name:{self.first_name}\n"
                               f"Last Name:{self.last_name}\n"
                               f"Address:{self.address}\n"
                               f"CNIC:{self.CNIC}")
                # for administrator details
                with open("Administrator.details.txt", "a+") as admin:
                    admin.write(f"              {self.username}(Saving_Account)\n"
                                f"Username:{self.username}\n"
                                f"Password:{self.password}\n"
                                f"First Name:{self.first_name}\n"
                                f"Last Name:{self.last_name}\n"
                                f"Address:{self.address}\n"
                                f"CNIC:{self.CNIC}\n\n\n")
            elif self.acc_type == 3:
                infoFile.write(f"                {self.username}(Loan_Account)\n"
                               f"Username:{self.username}\n"
                               f"Password:{self.password}\n"
                               f"First Name:{self.first_name}\n"
                               f"Last Name:{self.last_name}\n"
                               f"Address:{self.address}\n"
                               f"CNIC:{self.CNIC}")
                # for administrator details
                with open("Administrator.details.txt", "a+") as admin:
                    admin.write(f"              {self.username}(Loan_Account)\n"
                                f"Username:{self.username}\n"
                                f"Password:{self.password}\n"
                                f"First Name:{self.first_name}\n"
                                f"Last Name:{self.last_name}\n"
                                f"Address:{self.address}\n"
                                f"CNIC:{self.CNIC}\n\n\n")

        # New Account Charge
        print("Yearly Account Fee : 2000")
        self.init_deposit = float(input("Enter the initial deposit\Account Fee:"))
        if self.init_deposit >= 2000:
            with open("AccountNo.txt", "r+") as f:
                Account_No = f.read().split()
                self.account_No = int(Account_No[-1])
                self.account_No += 1
                f.write(str(self.account_No) + "\n")
            with open(f"{self.account_No}", "a+") as trans_file:
                if self.acc_type == 1:
                    trans_file.write(f"              {self.username}(Checking_Account)\n")
                elif self.acc_type == 2:
                    trans_file.write(f"              {self.username}(Saving_Account)\n")
                elif self.acc_type == 3:
                    trans_file.write(f"              {self.username}(Loan_Account)\n")
                self.init_deposit -= 2000
                from datetime import datetime
                dnt = datetime.now()
                trans_file.write(f"Date             Day           Balance\n")
                dnt = (f"{dnt.day}-{dnt.month}-{dnt.year}        {dnt.hour}:{dnt.minute}:{dnt.second}          ")
                trans_list=[dnt,self.init_deposit]
                for i in trans_list:
                    if i == trans_list [-1]:
                        trans_file.write(str(i)+"\n")
                    else:
                        trans_file.write(f"{i}")
            print("Your Account NO:", self.account_No)
            return True
        elif self.init_deposit <= 2000:
            print("Minimum initial deposit is 2000")

class Login:
    def login_info (self):
        self.username = input("Enter username:")
        self.accountNo = input("Enter your account No:")
        try:
            with open(f"{self.accountNo}","r") as f:
                pass
        except:
            print("Invalid username or password")
            return False
        else:
            print("Successfully Login\n")
            return True
class Checking_Account(Account):
    def __init__(self,balance=0,overdraft_fee=10000,credit_limit=-100000):
        super().__init__(balance)
        self.overdraft=overdraft_fee
        self.credit=credit_limit
    def deposit (self) :
        Acc_No = input("Enter account No:")
        self.dep = float(input("Enter the depositing Amount:"))
        with open(f"{Acc_No}", "r+") as f:
            Balance = f.read().split()
            self.balance = float(Balance[-1])
            if self.balance < 0:
                self.balance += self.dep
                if self.balance >= self.overdraft:
                    self.balance -= self.overdraft
                    from datetime import datetime
                    dnt = datetime.now()
                    dnt = (f"{dnt.day}-{dnt.month}-{dnt.year}        {dnt.hour}:{dnt.minute}:{dnt.second}          ")
                    trans_list = [dnt, self.balance]
                    for i in trans_list:
                        if i == trans_list[-1]:
                            f.write(str(i) + "\n")
                        else:
                            f.write(f"{i}")
                print(self.balance)
            else:
                self.balance += self.dep
                from datetime import datetime
                dnt = datetime.now()
                dnt = (f"{dnt.day}-{dnt.month}-{dnt.year}        {dnt.hour}:{dnt.minute}:{dnt.second}          ")
                trans_list = [dnt, self.balance]
                for i in trans_list:
                    if i == trans_list[-1]:
                        f.write(str(i) + "\n")
                    else:
                        f.write(f"{i}")
                print(self.balance)
    def withdraw (self) :
        Acc_No = input("Re-Enter account No: ")
        self.withdrawl=float(input("Enter the withdrawl Amount: "))
        with open(f"{Acc_No}", "r+") as f:
            Balance = f.read().split()
            self.balance = float(Balance[-1])
            if self.balance - self.withdrawl <= self.credit :
                print("You have reached the credit limit")
            else:
                self.balance -= self.withdrawl
                from datetime import datetime
                dnt = datetime.now()
                dnt = (f"{dnt.day}-{dnt.month}-{dnt.year}        {dnt.hour}:{dnt.minute}:{dnt.second}          ")
                trans_list = [dnt, self.balance]
                for i in trans_list:
                    if i == trans_list[-1]:
                        f.write(str(i) + "\n")
                    else:
                        f.write(f"{i}")
                print(self.balance)
    def Checking_Account_transaction(self):
        super().transaction()
    def Checking_Balance_Enquiery(self):
        super().balanceEnquiery()
    def Show_Account_details(self):
        super().show_Account_details()
    def show_Transaction_details(self):
        super().show_Transaction_details()
    def set_Credit_limit(self):
        self.credit=float(input("Set Credit_Limint:"))
    def set_Overdraft(self):
        self.overdraft=float(input("Set Overdraft:"))

class Saving_Account(Account):
    def __init__(self,balance=0,interest_rate=0.2):
        super().__init__(balance)
        self.interest_rate=interest_rate
    def deposit(self):
        super().deposit()
    def withdraw(self):
        Saving_Account.increase_balance(self)
        super().withdraw()
    def Saving_Account_Transaction(self):
        super().transaction()
    def Saving_Balance_Enquiery(self):
        super().balanceEnquiery()
    def Show_Account_details(self):
        super().show_Account_details()
    def show_Transaction_details(self):
        super().show_Transaction_details()
    def increase_balance(self):
        Acc_No = input("Enter account No: ")
        with open(f"{Acc_No}", "r+") as f:
            Balance = f.read().split("\n")
            Balance = Balance[-2]
            Balance = Balance.split()
            Balance = Balance[0]
            Balance = Balance.split("-")
            day = int(Balance[0])
            month = int(Balance[1])
            print(day)
            print(month)
            from datetime import datetime
            dnt = datetime.now()
            days = dnt.day - day
            months = (dnt.month - month)*30
            days += month
            if days >= 30:
                self.balance = f.seek(0)
                self.balance = f.read().split()
                self.balance = float(Balance[-1])
                self.balance += (self.balance * self.interest_rate)
                dnt = (f"{dnt.day}-{dnt.month}-{dnt.year}        {dnt.hour}:{dnt.minute}:{dnt.second}          ")
                trans_list = [dnt, self.balance]
                for i in trans_list:
                    if i == trans_list[-1]:
                        f.write(str(i) + "\n")
                    else:
                        f.write(f"{i}")
                print("Your Balance Become After Monthly_Interest_Rate :", self.balance)
    def set_interest_rate(self):
        self.interest_rate=float(input("Enter InterestRate__:"))
class Loan_Account(Account):
    def __init__(self,balance =0,Principal_amount =0,interest_rate =0.2,loan_duration = 12):
        super().__init__(balance)
        self.Principal_amount = Principal_amount
        self.interest_rate = interest_rate
        self.loan_duration = loan_duration
    def set_monthly_debit(self):
        self.Principal_amount=int(input("Enter Principal Amount:"))
        self.interest_rate += (self.Principal_amount * self.interest_rate)
        self.Principal_amount += self.interest_rate
        print(self.Principal_amount)
        self.monthly_debit_amount = self.Principal_amount/self.loan_duration
        print(f"You have to pay {self.monthly_debit_amount} Pkr. monthly ")
        Acc_No=input("Enter account No:")
        with open(f"{Acc_No}", "r+") as f:
            Balance = f.read().split()
            self.balance = float(Balance[-1])
            self.balance -= self.Principal_amount
            from datetime import datetime
            dnt = datetime.now()
            dnt = (f"{dnt.day}-{dnt.month}-{dnt.year}        {dnt.hour}:{dnt.minute}:{dnt.second}          ")
            trans_list = [dnt, self.balance]
            for i in trans_list:
                if i == trans_list[-1]:
                    f.write(str(i) + "\n")
                else:
                    f.write(f"{i}")
        print(self.balance)
    def deposit(self):
        Loan_Account.checking(self)
        Acc_No = input("Re_Enter your account No:")
        self.dep = float(input("Enter the depositing Amount:"))
        with open(f"{Acc_No}", "r+") as f :
            Balance = f.read().split()
            self.balance = float(Balance[-1])
            self.balance += self.dep
            from datetime import datetime
            dnt = datetime.now()
            dnt = (f"{dnt.day}-{dnt.month}-{dnt.year}        {dnt.hour}:{dnt.minute}:{dnt.second}          ")
            trans_list = [dnt, self.balance]
            for i in trans_list:
                if i == trans_list[-1]:
                    f.write(str(i) + "\n")
                else:
                    f.write(f"{i}")
        print(self.balance)
        with open(f"{Acc_No}", "r+") as check:
            balance = check.read().split()
            balance = float(balance[-1])
            if balance == 0:
                print("You successfully paid your loan amount!!!")
            else:
                pass

    def checking(self):
        Acc_No = input("Re_Enter your account No:")
        from datetime import datetime
        dnt = datetime.now()
        with open(f"{Acc_No}", "r+") as f:
            check_duration = f.read().split("\n")
            check_duration = check_duration[3]
            check_duration = check_duration.split()
            check_duration = check_duration[0]
            check_duration = check_duration.split("-")
            day = float(check_duration[0])
            month = float(check_duration[1])
            year = float(check_duration[2])
            total_days = dnt.day - day
            total_months = dnt.month - month
            total_days += total_months * 30
            total_years = dnt.year - year
            total_days += total_years * 360
            if total_days > (self.loan_duration*30):
                print("Time duration exceeded")
                self.interest_rate += 0.2
                print(f"Your loan amount increased to {self.interest_rate}")
                with open(f"{Acc_No}", "r+") as f:
                    Balance = f.read().split()
                    self.balance = float(Balance[-1])
                    self.balance += (self.balance * self.interest_rate)
                    print(self.balance)
                    from datetime import datetime
                    dnt = datetime.now()
                    dnt = (f"{dnt.day}-{dnt.month}-{dnt.year}        {dnt.hour}:{dnt.minute}:{dnt.second}          ")
                    trans_list = [dnt, self.balance]
                    for i in trans_list:
                        if i == trans_list[-1]:
                            f.write(str(i) + "\n")
                        else:
                            f.write(f"{i}")
    def Loan_Balance_Enquiery(self):
        super().balanceEnquiery()
    def Show_Account_details(self):
        super().show_Account_details()
    def show_Transaction_details(self):
        super().show_Transaction_details()
    def set_interst_rate(self):
        self.interestrate=float(input("Enter interest_rate:"))
    def set_loan_duration(self):
        self.loan_duration=int(input("Enter Loan Duration in months:"))
def Administrator():
    print("What you want to do:")
    print("1.To See All Users Details.\n2.To See Individual User Datails.\n"
          "3.To See User Transaction History.\n4.To Set Parameters.\n5.Exit\nPress Number According To Your Choice:\n ")
    while True:
        choice = int(input("Enter your choice:"))
        if choice == 1:
            with open("Administrator.details.txt", "r") as details:
                details = details.read()
                print(details)
        elif choice == 2:
            user = input("Enter CNIC No. of the User,You want see the details of:")
            with open(f"{user}", "r") as info:
                info = info.read()
                print(info)
        elif choice == 3:
            user_trans = input("Enter user account no you want to see the transaction history:")
            with open(f"{user_trans}", "r") as info:
                info = info.read()
                print(info)
        elif choice == 4:
            print("1.To Set Credit_Limit\n2.To Set Overdraft_Fee\n"
                  "3.To Set Saving Account Interest_Rate\n4.To Set Loan Account Interest_Rate\n"
                  "5.To Set Loan Duration\nPress Number According To Your Choice:")
            admin_input = int(input("Enter your choice:"))
            if admin_input == 1:
                ch_Account = Checking_Account()
                ch_Account.set_Credit_limit()
            elif admin_input == 2:
                ch_Account = Checking_Account()
                ch_Account.set_Overdraft()
            elif admin_input == 3:
                Sa_Account = Saving_Account()
                Sa_Account.set_interest_rate()
            elif admin_input == 4:
                L_Account = Loan_Account()
                L_Account.set_interst_rate()
            elif admin_input == 5:
                L_Account = Loan_Account()
                L_Account.set_loan_duration()
        elif choice == 5:
            print("Thank You!!!")
            break



print("*"*50,"WELCOME TO RBS BANK","*"*50)
print(f"                     1.Admin                         2.Customer")
choice = int(input("Press 1 if you are Admin & Press 2 if you are Customer:"))
if choice == 1:
    admin_pass = input("Enter your Password:")
    with open("Admin_pass.txt","r") as f:
        if f.readline() == admin_pass:
            print("Successfully Login!!\n")
            Administrator()
        else:
            print("Invalid Password")
elif choice == 2:
    print(f"\n                     1.Signup                        2.Login")
    OpenAccount = int(input("Press 1 for Signup & Press 2 for Login:"))
    if OpenAccount == 1:
        a = Customer()
        a.account_type()
    if OpenAccount == 2:
        a = Login()
        print("*"*30,"Press 1 for Checking_Account","*"*30)
        print("*"*30,"Press 2 for Saving_Account","*"*30)
        print("*"*30,"Press 3 for Loan_Account","*"*30)
        Acc_type = int(input("Enter your account_type:"))
        if Acc_type == 1:
            if a.login_info() == True:
                b = Checking_Account()
                print("Press 'T' for Transaction\nPress 'B' for Balance Enquiery\nPress 'D' for show_Basic_details")
                print("Press 'Y' for E-statement\nPress 'E' To Exit!\n")
                while True:
                    action = input("What you want to do:")
                    if action == "T":
                        b.Checking_Account_transaction()
                    elif action == "B":
                        b.Checking_Balance_Enquiery()
                    elif action == "D":
                        b.show_Account_details()
                    elif action == "Y":
                        b.show_Transaction_details()
                    elif action == "E":
                        print("Thank You!!")
                        break
            else:
                a.login_info()

        elif Acc_type == 2:
            if a.login_info() == True:
                b = Saving_Account()
                print("Press 'T' for Transaction\nPress 'B' for Balance Enquiery\nPress 'D' for show details")
                print("Press 'Y' for E-statement\nPress 'E' To Exit!!\n")
                while True:
                    action = input("What you want to do:")
                    if action == "T":
                        b.Saving_Account_Transaction()
                    if action == "B":
                        b.Saving_Balance_Enquiery()
                    if action == "D":
                        b.show_Account_details()
                    if action == "Y":
                        b.show_Transaction_details()
                    elif action == "E":
                        print("Thank You!!")
                        break
            else:
                a.login_info()
        if Acc_type == 3:
            if a.login_info() == True:
                c = Loan_Account()
                print("Press 'T' To Pay Loan Installment!\nPress 'B' To See Remaining Balance!\nPress 'D' For Account Details")
                print("Press 'Y' for E-statement\nPress 'E' To Exit!!\n")
                while True:
                    action = input("What you want to do:")
                    if action == "T":
                        c.deposit()
                    if action == "B":
                        c.Loan_Balance_Enquiery()
                    if action == "D":
                        c.show_Account_details()
                    if action == "Y":
                        c.show_Transaction_details()
                    elif action == "E":
                        print("Thank You!!")
                        break
            else:
                a.login_info()














