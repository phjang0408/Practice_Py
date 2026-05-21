d = {}
total = 0
n = int(input())
for _ in range(n):
    k = input()
    v = int(input())
    d[k] = v
print("Count : %d" % len(d))
for x in d.values(): # value들로 리스트 만들기 values, keys : 키들로 리스트만들기
    total += x
    
print("Total : %d" % total)