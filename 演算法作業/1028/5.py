class CreateBankAccount():
    def __init__(self,ID,name,count):
        self.id = ID
        self.name = name
        self.balance = count

    def deposit(self,amount):
        if amount<=0:
            print("失敗")
        else:
            self.balance += amount
            print("帳戶",self.name,"餘額=",self.balance)

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance -=amount
            print("帳戶",self.name,"餘額=",self.balance)
        else:
            print("失敗")

    def give(self,name,givemoney):
        self.withdraw(givemoney)
        name.deposit(givemoney)
        

id1=int(input("請輸入帳戶1之密碼= "))
name1=str(input("請輸入帳戶1之name= "))
id2=int(input("請輸入帳戶2之密碼= "))
name2=str(input("請輸入帳戶2之name= "))
count1 = 50000
count2 = 100000

account1 = CreateBankAccount(id1,name1,count1)
account2 = CreateBankAccount(id1,name2,count2)

a = int(input("請輸入帳戶1之存款金額"))
account1.deposit(a)
b=int(input("請輸入帳戶1之提款金額="))
account1.withdraw(b)
c=int(input("請輸入帳戶2之存款金額="))
account2.deposit(c)
d=int(input("請輸入帳戶2之提款金額="))
account2.withdraw(d)

givename = str(input("請輸入匯入帳戶(account1 or account2)= "))
givemoney = int(input("請輸入匯款金額= "))
if givename == 'account2':
    print('已匯款給帳戶2')
    account1.give(account2,givemoney)
else:
    print('已匯款給帳戶1')
    account2.give(account1,givemoney)
