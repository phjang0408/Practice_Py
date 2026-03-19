a = int(input())
b = int(input())
c = int(input())
if a > b:
    if c > a:
        print(a)
    elif c < a and c > b:
        print(c)
    else:
        print(b)
else:
    if c > b:
        print(b)
    elif c < b and c > a:
        print(c)
    else:
        print(a)