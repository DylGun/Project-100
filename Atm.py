class Atm:
    def __init__(self,atmcardnumber,pincardnumber):
        self.atmcardnumber=atmcardnumber
        self.pincardnumber=pincardnumber
    def CashWithdrawal(self):
        print("yourBalances")
    def BalanceInquiry(self):
        print("Inquiry")

Bank=Atm(20,1010)