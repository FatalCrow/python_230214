# class1.py
#클래스=원본, 인스턴스=복사본, 메서드=부품
#1)클래스 정의
class Person:
    #초기화 메서드
    def __init__(self):
        self.name = "default name"
        self.title = "new title"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
#()뜻 : __init__를 부름
p1 = Person()
p2 = Person()
p3 = Person()
p1.name = "전우치"
#3)메서드 호출
p1.print()
p2.print()
print(p3.title)

#동적으로 형식이 변경(추가)
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)