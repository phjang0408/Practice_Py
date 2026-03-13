# [유용한 함수]
a = 'hobby'
print(a.count('b')) # 문자 개수 세기, count
print(a.find('b'))  # 위치 찾기, find(없으면 -1)
print(a.index('y')) # 위치 찾기2, index(없으면 Error)

b = ",".join('abcd')# 삽입, join
print(b)

c = "Life is too short"
c = c.replace("Life", "Time") # 교체, replace
# 반환된 값을, 다시 대입해주어야 함
# upper 등을 수행해도, 변수 고유값은 변하지 않는다.
# 문자열은 '변경할 수 없는' 자료형이라, 대입문으로 바꿔야함
print(c)