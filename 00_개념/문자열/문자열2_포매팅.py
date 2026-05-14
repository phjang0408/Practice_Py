# [포매팅]
a = "I eat %d apples." % 3
print(a)
b = "I eat %s bananas" % "five"
print(b)
c = "I ate %d apples, %s bananas %%" %(7,"nine")
print(c)
# %s,%c,%d,%f,%% - 리터럴 % 그 자체
# 특히 %s는, 뒤에 정수나 소수를, 문자열로 바꾸어 대입

# [숫자와 사용]
e = "%10s" % "hello"
print(e)
f = "%0.4f" % 3.141592
print(f)

# [format 함수]
# 기본 index 형태(0부터 숫자로 나타내는 게 기본)
g = "I eat {0} apples".format(3)
print(g)
# name 형태(사용자 지정)
h = "I ate {number} apples, {count} bananas".format(number=10, count = "five")
print(h)