n = int(input())
li = []
for i in range(1,n+1):
    in_li = []
    for j in range(1,n+1):
        in_li.append(i*j)
    li.append(in_li)
print(li)