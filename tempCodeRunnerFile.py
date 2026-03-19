a = int(input())
a -= 3000
print("Buy Gift")
if(a > 1500):
    print("Buy Drink\n Money = %d" % a - 1500)
else:
    print("Money = %d" % a)