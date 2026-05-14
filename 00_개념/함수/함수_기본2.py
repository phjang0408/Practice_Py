# 여러개를 입력받는 함수
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

li = [1,2,3,4,5]
print(add_many(*li))