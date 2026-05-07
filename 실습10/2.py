# 최대공약수 찾기
def GCD(a,b):
    while b>0:
        temp = a
        a = b
        b = temp % b
    return a
a = int(input())
b = int(input())
print(GCD(a,b))