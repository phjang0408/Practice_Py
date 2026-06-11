countli=[0,0,0,0,0,0]
a = int(input())
b = int(input())
c = int(input())
d = int(input())
score = 0
li = [a,b,c,d]
li.sort()
for x in li:
    countli[x-1]+=1
if countli.count(4)>0:
    print(40)
elif (li[3]-1 == li[2] and li[2]-1 == li[1]) and li[1]-1 == li[0]:
    print(30)
elif countli.count(2) > 1:
    print(25)
elif countli.count(3) > 0:
    print(20)
elif (li[3]-1 == li[2] and li[2] - 1 == li[1]) or (li[2]-1 == li[1] and li[1]-1 == li[0]):
    print(15)
elif countli.count(2) == 1:
    print(10)
else:
    print(0)