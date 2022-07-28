class Atm:
    def __init__(self):
        self.card_number=""
        self.pin=""
        self.balance=1000
    def personalInfo(self):
        self.card_number=input("Enter Your CardNumber ")   
        self.pin=input("Enter Your PIN ") 
    def CheckBalance(self):
        print("Your Card Number is " + self.card_number)
        print("Your Balance is "+ str(self.balance))

    def Withdrawal(self):
        withdraw=int(input("Enter The Amount "))
        afterwith=self.balance-withdraw
        if afterwith>=0:
            print("Remaining Balance Is " + str(afterwith))
        else:
            print("Insufficient Balance")

atm=Atm()
atm.personalInfo()
atm.CheckBalance()
atm.Withdrawal()

        