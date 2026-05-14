n = int(input())
m = int(input())
li = []
for _ in range(n):
    mini_li = []
    for _ in range(m):
        x = int(input())
        mini_li.append(x)
    li.append(mini_li)
print(li)
