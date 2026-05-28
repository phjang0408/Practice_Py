dic = {"blue" : 2000, "black" : 3000, "yellow" : 5000}
total = 0
n = int(input())
for _ in range(n):
    eat = input()
    total += dic.get(eat)
if total >= 30000:
    total = total // 20 * 19
print(total)