n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
print(li)
r_li = []
for i in range(n,0,-1):
    r_li.append(li[i])
print(r_li)