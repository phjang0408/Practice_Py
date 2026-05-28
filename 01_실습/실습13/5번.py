n = int(input())
li = []
for _ in range(n):
    line = input().split()
    mini_li = [line[0]] + list(map(int,line[1:]))
    li.append(mini_li)
li.sort(key = lambda x : (-(x[1]+x[2]+x[3]), -x[1],-x[2], x[0]))

for p in li:
    name = p[0]
    score = sum(p[1:])
    print(f"{name} {score}")