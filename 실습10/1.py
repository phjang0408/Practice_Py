def sign_func(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    return a
n = int(input())
print(sign_func(n))