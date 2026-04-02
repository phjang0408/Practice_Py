total = 0
count = 0
while count < 5:
    ipt = int(input())
    count += 1
    total += ipt
    if ipt % 2 == 0:
        break
print("Total = %d" % total)
print("Count = %d" % count)