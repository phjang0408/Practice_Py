n = int(input())
Eng = []
Math = []
for i in range(n):
    Eng.append(int(input()))
    
for i in range(n):
    Math.append(int(input()))
    
for i in range(n):
    student_avg = (Eng[i] + Math[i]) / 2
    print(student_avg)