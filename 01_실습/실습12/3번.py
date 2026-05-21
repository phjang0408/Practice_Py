# 리스트 추가, 제거, 정렬
li = []
for _ in range(10):
    name = input()
    if name in li:
        li.remove(name)
    else:
        li.append(name)
li.sort()
for x in li:
    print(x)