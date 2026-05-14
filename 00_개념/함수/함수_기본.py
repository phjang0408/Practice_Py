# 함수 기본
def add(a,b):
    result = a + b
    return result

print(add(3,4))
a = add(5,6)
print(a)

# 입력값이 없는 함수
def say():
    return 'HI'

b = say()
print(b)

# 반환값이 없는 함수
def talk(a):
    print("%s 라고 말합니다" % a)
talk("안녕")