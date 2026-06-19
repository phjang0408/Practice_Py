a = [3,1,2]
a.sort()

b = ["banana", "apple", "kiwi"]
b.sort(key = len)

c = [-3, 1, -2]
c.sort(key = abs)

d = [(1, 3), (2, 1), (3, 2)]
d.sort(key = lambda x : x[1])
print(d)