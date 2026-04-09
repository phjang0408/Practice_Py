o = 0
x = 0
total = 0
while True:
    ipt = input()
    if ipt == "Finish":
        break
    elif ipt == 'X':
        x += 1
        total += 1
    elif ipt == 'O':
        o += 1
        total += 1
    
    
print("O : %d" % o)
print("X : %d" % x)
print("Rate : %.2f%%" % (o*100 / total))