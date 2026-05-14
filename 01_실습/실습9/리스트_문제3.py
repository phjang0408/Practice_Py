#학생의 수 정수 N을 입력받는다.
#N명의 국어 점수를 차례로 입력받고, 이후에 N명의 수학 점수를 차례로 입력받는다.
#학생 각각의 국어 점수와 수학 점수의 평균 점수를 출력한다.

n = int(input())
Eng = []
Math = []
for i in range(n):
    Eng.append(int(input()))
    
for i in range(n):
    Math.append(int(input()))
    
for i in range(n):
    student_avg = (Eng[i] + Math[i]) / 2
    print("%.1f"%student_avg)