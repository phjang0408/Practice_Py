import random
n = int(input())
m = int(input())
total = 0
for _ in range(50):
    x = random.randint(n,m)
    print(x)
    total += x
print("Avg : %.2f"%(total / 50))