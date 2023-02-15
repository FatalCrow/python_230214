# 정적메서드.py
# 인스턴스를 만들지 않고 클래스에서 바로 사용
class MyCalc(object):
    #데코레이터(살아있는 장식)
    @staticmethod
    def my_add(x,y):
        return x+y

#클래스에서 직접 호출한다.
a = MyCalc.my_add(5,7)
print(a)

