# 입력받아, 딕셔너리 구성하기
d = {}
n = int(input())
for _ in range(n):
    key = input()
    value = input()
    d[key]=value

cmd = input()
print(d[cmd])