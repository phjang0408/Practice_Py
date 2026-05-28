n = int(input())
li_t = []
li = []
for _ in range(n):
    tmp = int(input())
    li_t.append(tmp)
    if li.count(tmp) >0:
        continue
    else:
        li.append(tmp)
print(li_t)
print(li)