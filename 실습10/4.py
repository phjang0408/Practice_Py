li = []
total = 0
while len(li) != 5:
    x = int(input())
    total += x
    if x%5 == 0:
        li.append(x)
print(li)
print("Total : %d" % total)