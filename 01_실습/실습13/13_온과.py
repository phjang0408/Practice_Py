a = int(input("attendance = "))
b = int(input("assignment = "))
c = int(input("midterm = "))
d = int(input("final = "))
s = int(a*0.1+b*0.2+c*0.3+d*0.4)
print("Sum =",s)
if s >= 60:
    print("PASS")
else:
    print("FAIL")
