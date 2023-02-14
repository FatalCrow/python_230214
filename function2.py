#function2.py
print("---불변형식---")
a = 1.2
print (id(a))
a = 2.3
print(id(a))

print ("---가변형식---")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

x = 5
def func(a):
    return a+x

#호출
print (func(1))

def func2(a):
    x = 1
    return a+x
#호출

print(func2(1))

#교집합을 리턴하는 함수
def intersect(prelist, postlist):
    #지역변수에 교집합 문자 모으기
    result = []
    for x in prelist:
        if x in postlist and x not in result: 
            #if x in postlist = x의값이랑 postlist의 값이랑 일치하는 단어가 있는지 확인 (for문으로 첫번쨰 반복할때 H, 두번째 A, 세번째 M수행될때마다 SPAM이랑 비교)
            #not in = x in postlist 조건이 만족 되고 result값에 x값이 없으면 조건을 만족
            result.append(x)
    return result

#호출
print( intersect("HAM","SPAM"))

#전역변수에(불변) 읽기+쓰기
g = 1
def testScope(a):
    #global g
    g = 2
    return a+g

#호출
print(testScope(1))
print("전역변수 g:", g)

#가변형식
wordlist = ["J","A","M"]
def change(x):
    #복사본 생성
    x1 = x[:]
    #[:] = 복사본 만들때 사용됨
    x1[0] = "H"
    print("함수 내부:", x1)

#호출
change(wordlist)
print(wordlist)