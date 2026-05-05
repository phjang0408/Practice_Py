li = []
while True:
    a = int(input())
    if a == 0:
        break
    li.append(a)
print(sorted(set(li), reverse = True)[1])
