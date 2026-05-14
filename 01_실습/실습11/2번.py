# 제곱으로 리스트 채우고, 3의 배수만으로 새로운 리스트 만들기
N = int(input())
li = []
for i in range(1,N+1):
    li.append(i**2)
print(li)

li_3 = []
for x in li:
    if x % 3 == 0:
        li_3.append(x)
print(li_3)