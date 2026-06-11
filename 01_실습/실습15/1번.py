mountain = int(input())
course = int(input())
distance = int(input())
li = [0,1,0,2,2,1]
ti = li[(course - 1) * 3 + mountain - 1] * 5 + 10
print(distance* ti)