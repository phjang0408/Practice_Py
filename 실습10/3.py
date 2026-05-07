# abs함수
n = int(input())
total = 0.0
for _ in range(n):
    x = float(input())
    total += abs(x)
print("Total : %.2f"%total)