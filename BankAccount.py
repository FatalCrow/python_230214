# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #이름 숨김을 할시 self.__id, self.__name 이런식으로 __를 붙혀주면됨
        self.id = id
        self.name = name 
        self.balance = balance 
    #인스턴스 메서드
    def deposit(self, amount):
        self.balance += amount 
    def withdraw(self, amount):
        self.balance -= amount
    def __str__(self):
        return "{0}, {1}, {2}".format(self.id, 
        self.name, self.balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1)
#이름 숨김을 할시에 이름 규칙: _클래스명__변수명 , 클래스 외부에서는 아래와 같이 접근
#print(account1._BankAccount__balance)
#이름 숨김을 할시에 아래와 같이 하면 에러 발생
#print(account1.__balance)




